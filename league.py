# Get current standings in fantasy league
def get_standings(league_data):
      return league_data['standings']

# Returns the name of a fantasy league given the id
def get_league_name(league_data):
      league_name = league_data['name']
      return league_name

# Returns a list of classic leagues that a manager belongs to 
def get_manager_classic_leagues(manager_data):
      return manager_data['leagues']['classic']

# Returns a list of head to head leagues
def get_manager_h2h_leagues(manager_data):
      return manager_data['leagues']['h2h']

# Returns list of league name + ranking
def manager_leagues(manager_data):
      rankings = []
      for league in get_manager_classic_leagues(manager_data):
            rankings.append(f"{league['name']:<30}{league['entry_rank']}")
      return rankings