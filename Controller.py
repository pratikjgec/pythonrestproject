import requests
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to the App"

#Browser Url need to hit http://localhost:5000/first
@app.route('/first')
def getListEventTypes():
    url = "http://213.52.128.120/betfair_api/matchapi.php?Action=listEventTypes"
    resource = requests.get(url)
    jsonData = resource.json()
    return jsonify(jsonData)

#Browser url need to hit http:localhost:5000/second?eventTypeID=5
@app.route('/second')
def getListEventTypes1():
    eventTypeID = request.args.get('eventTypeID', default=1, type=str)
    url = "http://213.52.128.120/betfair_api/matchapi.php?Action=listCompetitions&EventTypeID="
    full_url = url + eventTypeID
    resource1 = requests.get(full_url)
    jsonDatawithEventType = resource1.json()
    return jsonify(jsonDatawithEventType)


#Browser url need to hit http://localhost:5000/third?eventTypeID=2&competitionID=12309951
@app.route('/third')
def getListEventTypes2():
    eventTypeID = request.args.get('eventTypeID', default=1, type=str)
    competitionID = request.args.get('competitionID', default=1, type=str)
    url = "http://213.52.128.120/betfair_api/matchapi.php?Action=listEvents&EventTypeID="+eventTypeID+"&"+"CompetitionID="+competitionID
    resource1 = requests.get(url)
    jsonDatawithEventType = resource1.json()
    return jsonify(jsonDatawithEventType)


#Browser url need to hit http://localhost:5000/forth?EventID=30299976
@app.route('/forth')
def getListwithEventId():
    eventId = request.args.get('EventID', type=str)
    url = "http://213.52.128.120/betfair_api/matchapi.php?Action=listMarketTypes&EventID="+eventId;
    resource1 = requests.get(url)
    jsonDatawithEventType = resource1.json()
    return jsonify(jsonDatawithEventType)

#Browser url need to hit http://localhost:5000/fifth?MarketID=1.165633879
@app.route('/fifth')
def getListwithMarketId():
    marketID = request.args.get('MarketID', type=str)
    url = "http://213.52.128.120/betfair_api/matchapi.php?Action=listMarketRunner&MarketID="+marketID;
    resource1 = requests.get(url)
    jsonDatawithEventType = resource1.json()
    return jsonify(jsonDatawithEventType)

#Browser url need to hit http://localhost:5000/sixth?MarketID=1.165633879
@app.route('/sixth')
def getListwithMarketId2():
    marketID = request.args.get('MarketID', default=1, type=str)
    url = "http://213.52.128.120/betfair_api/matchapi.php?Action=listRunnerBookFull&MarketID="+marketID;
    resource1 = requests.get(url)
    jsonDatawithEventType = resource1.json()
    return jsonify(jsonDatawithEventType)




@app.route('/dummyData')
def getApiData():
    url = "https://jsonplaceholder.typicode.com/todos/"
    data = requests.get(url)
    jsonData = data.json()
    print(jsonData)
    return jsonify(jsonData)


if __name__ == '__main__':
    app.run(debug=True)

