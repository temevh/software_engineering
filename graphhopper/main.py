from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("API_KEY")

route_url = "https://graphhopper.com/api/1/route?"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def geocoding(location, key):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key})
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code
    if json_status == 200 and len(json_data["hits"]) > 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        return json_status, lat, lng, name
    else:
        return json_status, None, None, location

class RouteRequest(BaseModel):
    start: str
    destination: str

@app.post("/api/route")
def get_route(route_request: RouteRequest):
    orig = geocoding(route_request.start, key)
    dest = geocoding(route_request.destination, key)

    if orig[0] == 200 and dest[0] == 200:
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])
        paths_url = route_url + urllib.parse.urlencode({"key": key}) + op + dp
        paths_response = requests.get(paths_url)
        paths_status = paths_response.status_code
        paths_data = paths_response.json()

        if paths_status == 200:
            miles = (paths_data["paths"][0]["distance"]) / 1000 / 1.61
            km = (paths_data["paths"][0]["distance"]) / 1000
            sec = int(paths_data["paths"][0]["time"] / 1000 % 60)
            min = int(paths_data["paths"][0]["time"] / 1000 / 60 % 60)
            hr = int(paths_data["paths"][0]["time"] / 1000 / 60 / 60)

            instructions = []
            for each in paths_data["paths"][0]["instructions"]:
                path = each["text"]
                distance_km = each["distance"] / 1000
                distance_miles = distance_km / 1.61
                instructions.append(
                    {
                        "instruction": path,
                        "distance_km": round(distance_km, 1),
                        "distance_miles": round(distance_miles, 1),
                    }
                )

            return {
                "status": "success",
                "start": orig[3],
                "destination": dest[3],
                "distance": {"miles": round(miles, 1), "km": round(km, 1)},
                "duration": f"{hr:02d}:{min:02d}:{sec:02d}",
                "instructions": instructions,
            }
        else:
            return {"status": "error", "message": paths_data.get("message", "Unknown error")}
    else:
        return {"status": "error", "message": "Failed to geocode one or both locations"}