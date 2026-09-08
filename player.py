import team as t
def get_player_name(player):
    name = f"{player['first_name']} {player['second_name']}"
    return name

# Returns the club name of a player
def get_player_club(clubs,player):
    club_id = player['team']
    return t.get_club_name(clubs,club_id)

def get_player_position(player):
    return None

# returns a player
def get_player(players,player_id):
    for player in players:
        if player['id'] == player_id:
            return player    
