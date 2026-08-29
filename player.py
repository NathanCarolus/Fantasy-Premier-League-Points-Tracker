import teams as ts
import team as t
def get_player_name(player):
    name = f"{player['first_name']} {player['second_name']}"
    return name

# Returns the club name of a player
def get_player_club(clubs,player):
    club_id = player['team']
    return ts.get_club_name(clubs,club_id)

def get_player_position(player):
    return None
