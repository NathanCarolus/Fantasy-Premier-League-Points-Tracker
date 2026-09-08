import players as ps
import player as p
# Returns the list of players for a manager in a given gameweek
def get_gameweek_picks(picks_data):
    return picks_data['picks']

# Returns the points scored by a player in a particular week
def get_live_points_lookup(live_data):
    return {p['id'] : p['stats']['total_points'] for p in live_data['elements']}

# Builds a report for the entire gameweek, for a particular manager
# Combines the picks for a GW, the results of the GW, and the respective player names
def get_squad_gameweek_report(picks_data,live_data,players):
    points_lookup = get_live_points_lookup(live_data)

    player_lookup = {p['id'] : p for p in players}

    report = []
    for pick in get_gameweek_picks(picks_data):
        player = player_lookup.get(pick['element'])
        if player is None:
            continue
        raw_points = points_lookup.get(pick['element'],0)
        applied_points = raw_points * pick['multiplier']
       # Adding a player to the dictionary
        report.append({'name': p.get_player_name(player),
                       'is_captain': pick['is_captain'],
                       'multiplier': pick['multiplier'],
                       'raw_points': raw_points,
                       'applied_points': applied_points})
    return report # Dictionary containing data about each player in the squad