import requests
import prompts 
import teams as ts
import team as t
import league
import players as ps
import player as p
import api
def main():
      option = 0
      fpl_data = get_fpl_data()                                                #API request for data 
      football_teams = ts.get_clubs(fpl_data)                                  #All football clubs
      football_players = ps.get_players(fpl_data)                              #All football players
     # league_data = get_league_data()
     # standings = league.get_standings(league_data)
    #  print_league_standings(standings)

      while option != -1:
            option = options()
            match option:
                  case -1:
                        print("Thank you for visiting")
                        exit()
                  case 1:
                        return None
                  case 2:
                        view_squad_list(football_teams,football_players)   
                        print("")
                  case 3:
                        search_for_player(football_teams,football_players)
                        print("")
                  case 4: 
                        return None
                  case 5: 
                        return None
                      

# Method to view all the players who belong to a certain squad
def view_squad_list(teams,players):
     ts.print_teams(teams)
     print("")
     team_name = input("Enter a team name: ")
     print("")
     team_id = t.get_team_id(teams,team_name)
     player_list = ps.get_players_in_team(players,team_id)
     if len(player_list) == 0:
           print("Team was not found")
           return
     for player in player_list:
          print(player)

# Method to find premier league 
def search_for_player(teams,players):
      player_name = input("Enter player name: ")
      player_list = []
      id = ps.get_player_id(players,player_name)

      while id != -1:
            player_list.append(ps.get_player(players,id))
      if len(player_list):
            print("No players found")
      else:
            for player in player_list:
                  print(p.get_player_club(teams,player))

#           API RELATED METHODS                 

# API Request for Teams and Players
def get_fpl_data():         
      return api.api_request("https://fantasy.premierleague.com/api/bootstrap-static/")

# API request to get data for a particular fpl squad
def get_squad_data(team_id):
      return api.api_request(f"https://fantasy.premierleague.com/api/entry/{team_id}/")

# API request for a particular league
def get_league_data(league_id):
      return api.api_request(f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/")

# API request foir a particular manager
def get_manager_data(manager_id):
      return api.api_request(f"https://fantasy.premierleague.com/api/entry/{manager_id}/")

# print league standings when standings is a json
def print_league_standings(standings):
      print("League standings")
      print(f"{'#':<5}{'Team Name':<25}{'ManagerName':<30}{'Total':<10}Team ID")
      for manager in standings['results']:
            rank = f"{manager['rank']}."
            print(f"{rank:<5}{manager['entry_name']:<25}{manager['player_name']:<30}{manager['total']:<10}{manager['entry']}")

# Displaying options      
def options():
      print("1. View Premier League Table")
      print("2. View Premier League Squad")
      print("3. Search for football players")
      print("4. View Fantasy Premier League Standings")
      print("5. View FPL manager Data")
      print("Enter -1 to exit")
      print("")
      return int(input("Select an option: "))
if __name__ == "__main__":
      main()