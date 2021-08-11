from json.decoder import JSONDecoder
from urllib.request import urlopen 
import urllib.parse
import json

def download_pegel_locations():
    with open("pegel_location.json", "w") as data:
        url = "www.pegelonline.wsv.de/webservices/rest-api/v2/stations.json"
        encoded_url = urllib.parse.quote(url)
        
        if not urllib.parse.urlparse(encoded_url).scheme:
            encoded_url = "https://" + encoded_url
            
        response = urlopen(encoded_url)
        
        data_json = json.loads(response.read())
        
        beautified_json = json.dumps(data_json, indent=4, sort_keys=True)
        
        data.write(beautified_json)
        
        print("Anzahl der Messstationen:", len(data_json))

# def filter_by_location(file, location):
def filter_by_location():
    with open("pegel_location.json", "r") as data:
        data_json = json.load(data)

        decoded_json = JSONDecoder.decode(data_json)

        print(decoded_json)

        #for i in data_json:
        #    print(i)

def parse_json_from_website(pegel_location):
    with open("data.json", "w") as data:
        url = "www.pegelonline.wsv.de/webservices/rest-api/v2/stations/" + pegel_location + "/W/measurements.json"
        encoded_url = urllib.parse.quote(url)
        
        if not urllib.parse.urlparse(encoded_url).scheme:
            encoded_url = "https://" + encoded_url
        
        response = urlopen(encoded_url)
        
        data_json = json.loads(response.read())
        
        beautified_json = json.dumps(data_json, indent=4, sort_keys=True)
        
        data.write(beautified_json)
        
        print(beautified_json)

def extract_values_from_json(file):
    pass

# user input
filter_by_location()
#location = input("Bitte den Ort des gewünschten Pegels eingeben: ")
#parse_json_from_website(location)