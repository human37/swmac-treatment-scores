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
    """Serves the main feed page for the user."""

    return render_template('feed.html')




@app.template_filter('convert_time')
def convert_time(ts):
    """A jinja template helper to convert timestamps to timeago."""
    return timeago.format(ts, time.time())

if __name__ == '__main__':
    app.secret_key = 'mygroup'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)