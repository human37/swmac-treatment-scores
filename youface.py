import time
import timeago
from flask import Flask, render_template, redirect, url_for, request, flash, make_response
from tinydb import TinyDB
import dbhelpers
import rankgraph
from flask import Flask, render_template
from geographyscore import geography_Score
from locationscore import location_Score
from tempscore import temperature_Score

__title__ = 'SWMAC Mosquito Ranking System'
__subtitle__ = 'Developed by students from Dixe State University'

app = Flask('youface')
db = TinyDB('db.json')

@app.after_request
def set_response_headers(response):
    # forces flask to not cache static images
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

def score(station, geography, temperature):
    tempscore = temperature_Score(int(temperature))
    geoscore = geography_Score(geography)
    stationscore = location_Score(station)
    return 100 * round(((tempscore + geoscore + stationscore) / 3), 3)

@app.route('/')
def index():
    f = open('stations.txt', 'r')
    choices_stations = ['Select here:']
    for line in f:
        choices_stations.append(line.strip())
    f.close()
    choices_geography = ['Select here:', 'Pond', 'Creek', 'Farmland', 'Residential', 'Marshland']
    # serves the main feed page for the user
    return render_template('feed.html', choices = choices_geography, stations = choices_stations)

@app.route('/submitdata' , methods = ['POST'])
def submit():
    # recieves the answers to the questions from the forms
    question1 = request.form.get('q1')
    question2 = request.form.get('q2')
    question3 = request.form.get('q3')
    # makes sure the whole form is completed correctly, and only integers are used for temperature
    if question1 == 'Select here:' or question2 == 'Select here:' or question3 not in '0123456789':
        if question3 == '':
            flash('Please complete all fields correctly!')
            return redirect(url_for('index'))
        try: 
            int(question3)
        except:
            flash('Please use only numbers for the temperature!')
            return redirect(url_for('index')) 
        flash('Please complete all fields correctly!')
    else:
        # adds them to the database
        dbhelpers.new_station_data(db, question1, question2, question3)
        flash('Station recorded successfully!')
    return redirect(url_for('index'))

@app.route('/rankdata' , methods = ['GET','POST'])
def rank():
    # gets all stations from the database, and calculates the score and ranks them
    stations = dbhelpers.get_stations(db)
    stations_list = []
    # ranks each station in the database
    for station in stations:
        name = station['q1']
        geography = station['q2']
        temperature = station['q3']
        score_num = score(name, geography, temperature)
        stations_list.append({'rank':None, 'q1':name, 'score':score_num})
    sorted_stations = sorted(stations_list, key = lambda i: (i['score']))
    for i in range(len(sorted_stations)):
        sorted_stations[i]['rank'] = len(sorted_stations) - i
    sorted_stations.reverse()
    # generates matplotlib graph and stores it in static/images/
    if len(sorted_stations) >= 1:
        # checks to see if there are any stations recorded, and if so it shows the graph
        rankgraph.saveGraph(sorted_stations)
        return render_template('rankedlist.html', stations = sorted_stations, plot_url = 'static/images/graph.png')
    return render_template('rankedlist.html', stations = sorted_stations)

@app.route('/resetlist', methods = ['POST'])
def reset():
    # clears all stations from the database, and deletes graph.png
    dbhelpers.reset_stations(db)
    flash('Station data reset successfully!')
    return rank()

@app.route('/moreinfo')
def infopage():
    return render_template('infopage.html')

@app.template_filter('convert_time')
def convert_time(ts):
    # a jinja template helper to convert timestamps to timeago
    return timeago.format(ts, time.time())

if __name__ == '__main__':
    app.secret_key = 'math4800' #used as the secret key for cookies
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)