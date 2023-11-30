import scrapper
import json

def test_getAllStations():
    assert len(json.loads(scrapper.getAllStations())) == 312

#data should exist using given arguments should 
def testExist_getTrains():
    assert len(json.loads(scrapper.getTrains("415","126"))) != 0

#data should be empty using given arguments 
def testEmpty_getTrain():
    assert len(json.loads(scrapper.getTrains("415","415"))) == 0
