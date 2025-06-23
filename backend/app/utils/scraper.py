import requests

def get_underdog_props():
    url = "https://api.underdogfantasy.com/over_under_lines"
    response = requests.get(url)
    return response.json()

def get_prizepicks_props():
    url = "https://api.prizepicks.com/projections"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response.json()
