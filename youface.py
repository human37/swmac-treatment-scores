import time
import timeago
from flask import Flask, render_template, redirect, url_for, request, flash, make_response
from tinydb import TinyDB
import dbhelpers

__title__ = 'SWMAC Mosquito Ranking System'
__subtitle__ = 'Developed by students from Dixe State University'

app = Flask('youface')
db = TinyDB('db.json')

@app.route('/')
def index():
    # serves the main feed page for the user
    return render_template('feed.html')

@app.route('/submitdata' , methods = ['POST'])
def submit():
    # recieves the answers to the questions from the forms
    question1 = request.form.get('q1')
    question2 = request.form.get('q2')
    question3 = request.form.get('q3')
    # adds them to the database
    dbhelpers.new_station_data(db, question1, question2, question3)
    return redirect(url_for('index'))

@app.route('/rankdata' , methods = ['GET','POST'])
def rank():
    # gets all stations from the database, and calculates the score and ranks them
    stations = dbhelpers.get_stations(db)
    return render_template('rankedlist.html', stations=stations)

@app.route('/resetlist', methods = ['POST'])
def reset():
    # clears all stations from the database
    dbhelpers.reset_stations(db)
    return rank()




@app.template_filter('convert_time')
def convert_time(ts):
    """A jinja template helper to convert timestamps to timeago."""
    return timeago.format(ts, time.time())

if __name__ == '__main__':
    app.secret_key = 'mygroup'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)