import requests
from bs4 import BeautifulSoup as bs
import json

sntfUrl = "https://www.sntf.dz/"
departureStations = []
arrivalStations = []

#scrape the web page to extract all stations
def scrape(url):
    sntf_page = requests.get(url).content

    soup = bs(sntf_page, "lxml")

    departureOptions = soup.find("select", id="gd")
    arrivalOptions = soup.find("select", id="ga")

    for option in departureOptions.find_all("option"):
        gare = {"id": option["value"],
               "name": option.text}
        departureStations.append(gare)
    departureStations.pop(0)


    for option in arrivalStations.find_all("option"):
        gare = {"id": option["value"],
               "name": option.text}
        arrivalStations.append(gare)
    arrivalStations.pop(0)

    #returns all stations as JSON
    def getAllStations():
        return json.dumps(departureStations)

    #returns list of trains of the given stations as JSON
    def getTrains(departureStation, arrivalStation):

        return
    

if __name__ == "__main__" :
    scrape(sntfUrl)
    
