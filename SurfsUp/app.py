# Import the dependencies.

import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app= Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes"""
    return(
        f"Available API Routes :</br>"
        f"/api/v1.0/precipitation:</br>"
        f"/api/v1.0/stations:</br>"
        f"/api/v1.0/tobs:</br>"
        f"/api/v1.0/<start>: </br>"
        f"/api/v1.0/<start>/<end>: </br>"
    )
#Station Data
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    # Query all Station data 
    Station_Data = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    List_Stations = list(np.ravel(Station_Data))
    #Return list of jsonified Station Data
    return jsonify(List_Stations)
    sess
# Precipitation Analysis
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Get the precipitation data for 12 months prior to the latest date"""
    # Query all precipitation data 
    last_date=session.query(func.max(Measurement.date)).first()[0]
    query_date = dt.datetime.strptime(last_date,"%Y-%m-%d") - dt.timedelta(days=365)
    Precipitation_Data = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= query_date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of Precipitation Data
    precipitation_list = []
    for date,prcp in Precipitation_Data:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation_list.append(precipitation_dict)

    return jsonify(precipitation_list)
#Tobs data
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Get the tobs data for 12 months prior to the latest date """
    # Query all tobs data 
    last_date_tobs=session.query(func.max(Measurement.date)).first()[0]
    query_date_tobs = dt.datetime.strptime(last_date_tobs,"%Y-%m-%d") - dt.timedelta(days=365)
    Tobs_Data = session.query(Measurement.date,Measurement.tobs).filter(Measurement.station =='USC00519281').\
                        filter(Measurement.date >=query_date_tobs).all()

    session.close()

    # Create a dictionary from the row data and append to a list of Tobs Data
    tobs_list = []
    for date,tobs in Tobs_Data:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)



@app.route("/api/v1.0/<start>")
def startd(start = None):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    #Create a list to calculate Min, Average and Maximum temperature
    Temperature_List_1 = [func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)]
    #Query

    Start_End = session.query(*Temperature_List_1).filter(Measurement.date >= start).all()
    session.close()
    Start_End_data = list(np.ravel(Start_End))
    return jsonify(Start_End_data)

@app.route("/api/v1.0/<start>/<end>")
def startend(start = None , end = None):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    #Create a list to calculate Min, Average and Maximum temperature
    Temperature_List = [func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)]
    #Query

    Start_End_d = session.query(*Temperature_List).filter(Measurement.date >= start).\
                        filter(Measurement.date <= end).all()
    session.close()
    Start_End_data = list(np.ravel(Start_End_d))
    return jsonify(Start_End_data)
    


if __name__ == '__main__':
    app.run(debug=True)