import datetime as dt
from turtle import end_fill
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from sympy import stationary_points

#The create_engine() function allows us to access and query 
# our SQLite database file

engine = create_engine("sqlite:///hawaii.sqlite")

#  reflect the database into our classes.
Base = automap_base()

Base.prepare(engine, reflect = True)

# With the database reflected,
#  we can save our references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to our database
session = Session(engine)

app= Flask(__name__)

@app.route('/')

def welcome():

    return(
    '''

    Welcome to the Climate Analysis API!

    Available Routes:

    /api/v1.0/precipitation

    /api/v1.0/stations
    
    /api/v1.0/tobs

    /api/v1.0/temp/start/end

    ''')

@app.route("/api/v1.0/precipitation")
def precipitation():

    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

    precip = {date: prcp for date, prcp in precipitation}

    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():

    results = session.query(Station.station).all()

    stations = list(np.ravel(results))

    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():

    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prev_year).all()

    temps = list(np.ravel(results))

    return jsonify(temp=temps)

@app.route("/api/v1.0/temp/<start>")

@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start = None, end = None):

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:

        results = session.query(*sel).filter(Measurement.date >= start).all()

        temps = list(np.ravel(results))

        return jsonify(temps)

    results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <=end).all()

    temps = list(np.ravel(results))

    return jsonify(temps)