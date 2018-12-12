#import dependencies
import numpy as np

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData
from sqlalchemy.pool import StaticPool

from flask import Flask, jsonify

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

engine = create_engine("sqlite:///Resources/hawaii.sqlite",
    connect_args={'check_same_thread':False},
    poolclass=StaticPool)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our connection object
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        "<img src=\"https://img.etimg.com/thumb/msid-46065787,width-300,imgsize-83533,resizemode-4/7-things-mobile-app-developers-should-focus-on.jpg\" alt=\"mobile-apps\" width=\"800\" height=\"300\"/>"+
        "<br/>"+
        "<br/>"+
        "Available Routes:<br/>" +
        "<br/>"+
        "/api/v1.0/precipitation<br/>"+
        "Return a list of all dates and precipitation<br/>"+
        "<br/>"+
        "/api/v1.0/stations<br/>"+
        "Return a list of stations data<br/>"+
        "<br/>"+
        "/api/v1.0/tobs<br/>"+
        "Return a list of Temperature Observations (tobs) for the previous year<br/>"+
        "<br/>"+
        "/api/v1.0/<start><br/>"+
        "When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.<br/>"+
        "<br/>"+
        "/api/v1.0/<start>/<end>"
        "When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.<br/>"
    )