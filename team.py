import player as p
# returns a list of players in a particular team
def get_players_in_team(players,team_id):
    player_name_list = []
    for player in players:
        if player['team'] == team_id:
            player_name_list.append(p.get_player_name(player))
    return player_name_list

#Returns the id field given a specific team name
def get_team_id(teams,team_name):
      for team in teams:
            if (team_name.lower() == team['name'].lower()) or (team_name.lower() == team['short_name'].lower()):
             return team['id']

# returns the club name 
def get_team_name(teams, team_id):
    for team in teams:
        if team['id'] == team_id:
            return team['name']