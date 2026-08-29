import player as p
def get_players(data):
      return data['elements']
# returns a player
def get_player(players,player_id):
    for player in players:
        if player['id'] == player_id:
            return player    

# returns the ID of the respective player
def get_player_id(players, player_name):
    for player in players:
        if (player['first_name'] or player['second_name'] or player['web_name'] or player['known_name']) == player_name:
            return player['id']
    else:
        return -1
    
def get_players_in_team(players,team_id):
    player_name_list = []
    for player in players:
        if player['team'] == team_id:
            player_name_list.append(p.get_player_name(player))
    return player_name_list