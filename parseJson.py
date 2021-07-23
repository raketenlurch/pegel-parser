from urllib.request import urlopen 
import urllib.parse
import json

def parse_json_from_website(pegel_location):
    with open("data.txt", "w") as data:
        url = "www.pegelonline.wsv.de/webservices/rest-api/v2/stations/" + pegel_location + "/W/measurements.json"
        encoded_url = urllib.parse.quote(url)
        
        if not urllib.parse.urlparse(encoded_url).scheme:
            encoded_url = "https://" + encoded_url
        
        response = urlopen(encoded_url)
        
        data_json = json.loads(response.read())
        
        beautified_json = json.dumps(data_json, indent=4, sort_keys=True)
        
        data.write(beautified_json)
        
        print(beautified_json)