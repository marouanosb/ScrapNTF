import requests
from bs4 import BeautifulSoup as bs
import json
import datetime

sntfUrl = "https://www.sntf.dz/"

#scrape the web page form to extract all stations
def scrapeStations(url):
    sntf_page = requests.get(url).content

    soup = bs(sntf_page, "lxml")
    stationsOptions = soup.find("select", id="gd")

    stations = []
    for option in stationsOptions.find_all("option"):
        gare = {"id": option["value"],
               "name": option.text}
        stations.append(gare)

     #delete the first element which is the select default text
    stations.pop(0)

    return stations


#scrape the result list web page to extract all trains
def scrapeTrains(departureStationValue,arrivalStationValue,date):

    #format the date to pass in the request format "yyyyMMdd"
    strDate = str(date.year) + str(date.month) + str(date.day)
    
    trainsUrl = sntfUrl + f"index.php/component/sntf/?gd={departureStationValue}&ga={arrivalStationValue}&dd={strDate}&h1=0000&h2=2359&view=train"
    trains_page = requests.get(trainsUrl).content

    soup = bs(trains_page, "lxml")
    trainsDetailsDivs = soup.find_all("div", class_="col-xs-7 mob_train_body")

    #if there are no trains for the given stations
    if len(trainsDetailsDivs) == 0:
        return []
    
    #to replace the eventual extra spaces (\t\r\n) with None
    characters_to_remove = {'\t': None, '\r': None, '\n': None}

    trains = []
    for div in trainsDetailsDivs:
        train = {"id": div.contents[1].text,
                 "type": div.contents[3].text,
                 "departureStation": div.contents[5].text,
                 "departureTime": div.contents[7].text,
                 "arrivalStation": div.contents[9].text,
                 "arrivalTime": div.contents[11].text}
        
        #remove extra spaces using maketrans (translate)
        for key in train:
            train[key] = train[key].strip().translate(str.maketrans(characters_to_remove))

        trains.append(train)

    return trains


#returns all stations as JSON
def getAllStations():
    stations = scrapeStations(sntfUrl)

    #"ensure_ascii=False" to disable converting special characters (é/à...etc) to ascii code
    return json.dumps(stations, ensure_ascii=False, indent=4)


    #returns list of trains of the given stations as JSON
def getTrains(departureStation, arrivalStation, date = datetime.date.today()):
    trains = scrapeTrains(departureStation,arrivalStation, date)

    #"ensure_ascii=False" to disable converting special characters (é/à...etc) to ascii code
    return json.dumps(trains, ensure_ascii=False, indent=4)


#passes through all the station and return all train schedules 
def getAllTrains(date):
    stations = scrapeStations(sntfUrl)

    allTrains = []
    for departureStation in stations:
        for arrivalStation in stations:
            if departureStation == arrivalStation: 
                continue    #do nothing if departure and arrival station are the same
            trains = scrapeTrains(departureStation["id"],arrivalStation["id"], date)
            print(f"{len(trains)} trains found for {departureStation['name']} -> {arrivalStation['name']}")
            if(trains == []):
                continue    #do nothing if there are no trains for given stations
            allTrains.append(trains)
    
    return json.dumps(allTrains, ensure_ascii=False, indent=4)