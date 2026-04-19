
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

matches = [
    {"id":1,"home":"Arsenal","away":"Chelsea","date":"2026-04-20","time":"18:00"},
    {"id":2,"home":"Barcelona","away":"Real Madrid","date":"2026-04-21","time":"20:00"},
    {"id":3,"home":"Liverpool","away":"Man City","date":"2026-04-22","time":"19:00"}
]

@app.get("/matches")
def get_matches():
    return matches

@app.get("/prediction/{match_id}")
def prediction(match_id:int):
    return {
        "home":50,
        "draw":20,
        "away":30,
        "reason":"Better recent form and home advantage"
    }
