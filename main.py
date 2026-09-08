import prompts as prompt
import teams as ts
import team as t 
import league
import players as ps
import player as p
import api
import gameweek as gw
import manager
def main():
      option = 0
      fpl_data = get_fpl_data()                                                #API request for data 
      football_teams = ts.get_teams(fpl_data)                                  #All football clubs
      football_players = ps.get_players_data(fpl_data)                              #All football players
     # league_data = get_league_data()
     # standings = league.get_standings(league_data)
    #  print_league_standings(standings)

      while option != -1:
            options()
            option = int(prompt.get_option())
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
                        
                        manager_id = input("Enter manager ID: ")
                        view_manager_profile(manager_id)
                        manager_data = get_manager_data(manager_id)
                        if input("View leagues (Y/N)?: ") == "Y":
                              print_manager_leagues(manager_data)
                        if input("View gameweek (Y/N)?: ") == "Y":
                              gameweek_id = int(prompt.gameweek_id())
                              print("")
                              print(f"SQUAD FOR GAMEWEEK {gameweek_id}")
                              print("")
                              live_data = get_gameweek_data(gameweek_id)
                              picks_data = get_picks_data(manager_id,gameweek_id)
                              report = gw.get_squad_gameweek_report(picks_data,live_data,football_players)
                              print("")
                              print_squad_gameweek_report(report)
                              print("")
                              
                      

# Method to view all the players who belong to a certain squad
def view_squad_list(teams,players):
     print_teams(teams)
     print("")
     team_name = prompt.team_name()
     print("")
     team_id = t.get_team_id(teams,team_name)
     player_list = t.get_players_in_team(players,team_id)
     if player_list == None:
           print("Team was not found")
           return
     for player in player_list:
          print(p.get_player_name(player))

# Method to find current Premier League Players 
def search_for_player(teams,players):
      player_name = prompt.player_name()
      print()

      player_list = ps.get_players(players,player_name)

      if  player_list == None:
            print("No players found")
      else:
            for player in player_list:
                  print(f"{p.get_player_name(player):<35}{p.get_player_club(teams,player)}")


def view_manager_profile(manager_id):
      manager_data = get_manager_data(manager_id)

      print(f"Name: {manager.get_manager_name(manager_data)}")
      print(f"Country: {manager.get_manager_country(manager_data)}")
      print(f"Team Name: {manager.get_manager_team_name(manager_data)}")
      print("")



#           API RELATED METHODS                 

# API Request for Teams and Players
def get_fpl_data():         
      return api.get_fpl_data()

# Returns squad data
def get_squad_data(squad_id):
      return api.get_squad_data(squad_id)

# Returns league data
def get_league_data(league_id):
      return api.get_league_data(league_id)

# Returns manager data
def get_manager_data(manager_id):
      return api.get_manager_data(manager_id)

# get data for a managers picks
def get_picks_data(manager_id,gameweek_id):
      return api.get_manager_gameweek_data(manager_id,gameweek_id)

# Returns the data for a specific game week
def get_gameweek_data(gameweek_id):
      return api.get_live_gameweek_data(gameweek_id)

#           PRINTING RELATED METHODS  

# game week report    
def print_squad_gameweek_report(report):
      print(f"{'Player':<30}{'Cap':<5}{'Mult':<6}{'Raw Pts':<9}Applied Pts")
      for entry in report:
            cap = "(C)" if entry['is_captain'] == True else ""
            print(f"{entry['name']:<30}{cap:<5}{entry['multiplier']:<6}{entry['raw_points']:<9}{entry['applied_points']}")

# Prints the leagues that the respective manager is in
def print_manager_leagues(manager_data):
      rankings = league.manager_leagues(manager_data)
      for rank in rankings:
            print(rank)

# Displaying options      
def options():
      print("1. View Premier League Table")
      print("2. View Premier League Squad")
      print("3. Search for football players")
      print("4. View Fantasy Premier League Standings")
      print("5. View FPL manager Data")
      print("Enter -1 to exit")
      print("")

# print all teams 
def print_teams(teams):
      for team in teams:
            print(team['name'])

# print league standings when standings is a json
def print_league_standings(standings):
      print("League standings")
      print(f"{'#':<5}{'Team Name':<25}{'ManagerName':<30}{'Total':<10}Team ID")
      for manager in standings['results']:
            rank = f"{manager['rank']}."
            print(f"{rank:<5}{manager['entry_name']:<25}{manager['player_name']:<30}{manager['total']:<10}{manager['entry']}")
if __name__ == "__main__":
      main()