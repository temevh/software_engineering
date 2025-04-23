from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RouteRequest(BaseModel):
    start: str
    destination: str

@app.get("/api/message")
def get_message():
    return {"message": "Hello from FastAPI!"}

@app.post("/api/route")
def get_route(route_request: RouteRequest):
    message = f"Route from {route_request.start} to {route_request.destination}"
    return {"message": message}