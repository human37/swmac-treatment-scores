import time
from tinydb import Query

def new_station_data(db, q1, q2, q3):
    station_data = db.table('stations')
    return station_data.insert({'q1': q1, 'q2': q2, 'q3':q3, 'time': time.time()})

def get_stations(db):
    station_data = db.table('stations')
    stations = station_data.all()
    return stations

def reset_stations(db):
    station_data = db.table('stations')
    station_data.purge()