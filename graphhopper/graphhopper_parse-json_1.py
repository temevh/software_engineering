import requests
import urllib.parse 
import os
from dotenv import load_dotenv

load_dotenv() 

key = os.getenv("API_KEY")

route_url = "https://graphhopper.com/api/1/route?"

def geocoding (location, key):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1",
    "key":key})
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code
    if json_status == 200:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]

        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country=""

        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state=""

        if len(state) !=0 and len(country) !=0:
            new_loc = name + ", " + state + ", " + country
        elif len(state) !=0:
            new_loc = name + ", " + country
        else:
            new_loc = name

            print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n"
            + url)
    else:
        lat="null"
        lng="null"
        new_loc=location
    return json_status,lat,lng,new_loc 

while True:
    loc1 = input("Starting Location: ")
    if (loc1 == "quit" or loc1 == "q"):
        break
    orig = geocoding(loc1, key)
    print(orig)
    loc2 = input("Destination: ")
    if (loc2 == "quit" or loc2 == "q"):
        break
    dest = geocoding(loc2, key)
    print(dest)