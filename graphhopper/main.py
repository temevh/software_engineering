from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS setup (important if frontend and backend are on different ports!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to the specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/message")
def get_message():
    return {"message": "Hello from FastAPI!"}
