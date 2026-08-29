# Prints all teams  data -> json
def print_teams(clubs):
        for club in clubs:
            print(club['name'])

def get_teams(data):
       return data['teams']

#Returns the id field given a specific team name
def get_teams_id(clubs,club_name):
      for club in clubs:
            if (club_name.lower() == club['name'].lower()) or (club_name.lower() == club['short_name'].lower()):
             return club['id']

# returns the club name 
def get_teams_name(clubs, club_id):
    for club in clubs:
        if club['id'] == club_id:
            return club['name']