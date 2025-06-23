from fastapi import APIRouter
from app.utils.db import get_player_stats
from app.utils.scraper import get_underdog_props, get_prizepicks_props

router = APIRouter()

@router.get("/player_stats/{sport}/{player_name}")
def api_get_player_stats(sport: str, player_name: str):
    return {"data": get_player_stats(sport, player_name)}

@router.get("/live_props/{source}")
def live_props(source: str):
    if source == "underdog":
        return get_underdog_props()
    elif source == "prizepicks":
        return get_prizepicks_props()
    else:
        return {"error": "Invalid source"}

@router.get("/recommended_props/{sport}")
def get_top_props(sport: str):
    historical_avg = {"LeBron James": {"points": 27.4}}
    live_line = {"LeBron James": {"points": 25.5}}
    suggestions = []
    for player in live_line:
        for stat in live_line[player]:
            if historical_avg[player][stat] > live_line[player][stat]:
                suggestions.append({
                    "player": player,
                    "stat": stat,
                    "pick": "higher",
                    "line": live_line[player][stat],
                    "average": historical_avg[player][stat]
                })
    return {"recommendations": suggestions}
