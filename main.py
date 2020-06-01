import time
import timeago
from flask import Flask, render_template, redirect, url_for, request, flash, make_response
from tinydb import TinyDB
import dbhelpers
import rankgraph
import scoring_algorithm

__title__ = 'SWMAC Mosquito Ranking System'
__subtitle__ = 'Developed by students from Dixe State University'

app = Flask('youface')
db = TinyDB('db.json')

def setup(temperature):
    # clears out any existing stations in the database
    dbhelpers.reset_stations(db)
    # reads from stations.txt into Station objects
    f = open('stations.txt', 'r')
    station_objects = []
    for line in f:
        line = line.split()
        station = scoring_algorithm.Station(line[1], line[0])
        station_objects.append(station)
    f.close()
    # adds each station into the database
    for station in station_objects:
        dbhelpers.new_stations(db, station, temperature)

def rank():
    # gets all stations from the database
    stations = dbhelpers.get_stations(db)
    stations_list = []
    # ranks each station in the database
    for station in stations:
        name = station['location']
        score_num = station['score']
        stations_list.append({'rank' : None, 'location' : name, 'score' : score_num})
    sorted_stations = sorted(stations_list, key = lambda i: (i['score']))
    for i in range(len(sorted_stations)):
        sorted_stations[i]['rank'] = len(sorted_stations) - i
    sorted_stations.reverse()
    return sorted_stations

@app.after_request
def set_response_headers(response):
    # forces flask to not cache static images
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def index():
    # serves the main feed page for the user
    return render_template('feed.html')

@app.route('/submit_temperature' , methods = ['POST'])
def submit_temperature():
    # recieves the answers to the questions from the forms
    temperature = request.form.get('temperature_input')
    # makes sure  only numbers are used for temperature
    if temperature == None or not temperature.isdigit():
        flash('Please use only numbers for the temperature!')
        return redirect(url_for('index')) 
    else:
        # clears out any existing records
        dbhelpers.reset_temperature(db)
        # converts to celsius
        celsius_temperature = (int(temperature) - 32) * 5/9
        # adds the new temperature to the database
        dbhelpers.new_temperature(db, celsius_temperature)
        # adds all stations to the database and rescores with new temperature
        setup(celsius_temperature)
        flash('Scores generated successfully!')
    return redirect(url_for('index'))

@app.route('/treatment', methods = ['GET'])
def input_treatment():
    # gets all stations and renders treatment.html
    stations = dbhelpers.get_stations(db)
    return render_template('treatment.html', stations = stations)

@app.route('/submit_treatment' , methods = ['POST'])
def submit_treatment():
    # recieves specific station and records in the treatments table
    treated_station = request.form.get('treatment_input')
    all_treatments = dbhelpers.get_treatments(db)
    for station in all_treatments:
        if treated_station == station['station']:
            flash('This station has already recieved treatment within the past 3 days')
            return input_treatment()
    dbhelpers.new_treatment(db, treated_station)
    flash("Treatment information was updated successfully!")
    return input_treatment()

@app.route('/ranklisting' , methods = ['GET','POST'])
def rank_list():
    sorted_stations = rank()
    return render_template('rankedlist.html', stations = sorted_stations)

@app.route('/resetlist', methods = ['POST'])
def reset_list():
    # clears all stations from the database
    dbhelpers.reset_stations(db)
    flash('Station data reset successfully!')
    return rank_list()

@app.route('/rankgraph' , methods = ['GET','POST'])
def rank_graph():
    # gets all stations from the database, and ranks them and generates a graph
    sorted_stations = rank()
    if len(sorted_stations) == 0:
        return render_template('rankedgraph.html')
    rankgraph.saveGraph(sorted_stations)
    return render_template('rankedgraph.html', stations = sorted_stations, plot_url = 'static/images/graph.png')

@app.route('/resetgraph', methods = ['POST'])
def reset_graph():
    # clears all stations from the database
    dbhelpers.reset_stations(db)
    flash('Station data reset successfully!')
    return rank_graph()

@app.route('/moreinfo')
def infopage():
    return render_template('infopage.html')

@app.template_filter('convert_time')
def convert_time(ts):
    # a jinja template helper to convert timestamps to timeago
    return timeago.format(ts, time.time())

if __name__ == '__main__':
    # used as the secret key for cookies
    app.secret_key = 'math4800' 
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)