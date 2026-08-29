# returns a list of players in a particular team
def get_players_in_team(players,team_id):
    player_name_list = []
    for player in players:
        if player['team'] == team_id:
            player_name_list.append(p.get_player_name(player))
    return player_name_list
