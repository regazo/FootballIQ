
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
import requests

@app.get("/real-matches")
def get_real_matches():
    url = "https://api.football-data.org/v4/matches?status=SCHEDULED"

    headers = {
        "X-Auth-Token": "2cb64b0370eb46b0b841929f95fd8e6a"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    matches = []

    for m in data.get("matches", [])[:15]:
        matches.append({
            "id": m["id"],
            "home": m["homeTeam"]["name"],
            "away": m["awayTeam"]["name"],
            "date": m["utcDate"][:10],
            "time": m["utcDate"][11:16],
            "competition": m["competition"]["name"],
            "status": m["status"],
            "homeLogo": m["homeTeam"].get("crest", ""),
            "awayLogo": m["awayTeam"].get("crest", "")
        })

    return matches
