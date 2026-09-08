import requests
# Helper function performating API request given a URL
def api_request(url):
      response = requests.get(url)
      if response.status_code == 200:
            return response.json()
      else:
            print(f"Error: Unable to fetch data (Status Code:{response.status_code})")
            return None
# API request for an fpl manager
def get_manager_data(manager_id):
      return api_request(f"https://fantasy.premierleague.com/api/entry/{manager_id}/")

# API request for an fpl league
def get_league_data(league_id):
      return api_request(f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/")

# API request for an fpl managers particular squad in a given GW
def get_squad_data(manager_id,gameweek_id):
      return api_request(f"https://fantasy.premierleague.com/api/entry/{manager_id}/event/{gameweek_id}/picks/")

# API request for general fpl data
def get_fpl_data():
      return api_request("https://fantasy.premierleague.com/api/bootstrap-static/")

# API request for live points data for a given gameweek
def get_live_gameweek_data(gameweek_id):
      return api_request(f"https://fantasy.premierleague.com/api/event/{gameweek_id}/live/")

# API request for data GW of a particular manager
def get_manager_gameweek_data(manager_id, gameweek_id):
      return api_request(f"https://fantasy.premierleague.com/api/entry/{manager_id}/event/{gameweek_id}/picks/")