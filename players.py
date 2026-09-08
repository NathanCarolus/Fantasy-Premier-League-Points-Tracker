import player as p

def get_players_data(data):
      return data['elements']

# returns a list of palyers the respective player name
def get_players(players, player_name):
    player_list = []
    name = player_name.lower()

    for player in players:
        first = str(player.get('first_name','')).lower()
        second = str(player.get('second_name','')).lower()
        known = str(player.get('known_name','')).lower()
        web = str(player.get('web_name','')).lower()
        if (first == name or 
            second == name or 
            known == name  or
            web == name):
            player_list.append(player)

    return player_list

