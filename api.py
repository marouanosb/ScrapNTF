import datetime
import json
from flask import Flask, request, jsonify
from scrapper import getAllStations, getTrains, getAllTrains
import json

app = Flask(__name__)
#make JSON response pretty
#app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route("/", methods = ['GET'])
def index():
    countStations = len(json.loads(getAllStations()))
    totalStationsText = f"{datetime.date.today()} with {countStations} total stations found."
    
    return totalStationsText

@app.route("/getAllStations/", methods = ['GET'])
def ReturnAllStation():
    allStations = getAllStations()
    
    return allStations

@app.route("/getTrains/", methods = ['GET'])
def ReturnTrains():
    departureStation = request.args.get("departureStation")
    arrivalStation = request.args.get("arrivalStation")
    trains = getTrains(departureStation, arrivalStation, datetime.date.today())

    return trains

@app.route("/getAllTrains/", methods = ['GET'])
def ReturnAllTrains():
    allTrains = getAllTrains(datetime.date.today())

    return allTrains


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
