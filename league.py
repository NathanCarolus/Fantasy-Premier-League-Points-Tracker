import api
# Get current standings in private private league
def get_standings(league_data):
      return league_data['standings']
# returns the name of a league given the id
def get_league_name(league_id):
      league_data = api.api_request(f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/")
      league_name = league_data['name']
      return league_name
      