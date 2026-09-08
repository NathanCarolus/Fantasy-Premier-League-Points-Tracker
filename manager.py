#  Returns manager's full name
def get_manager_name(manager_data):
    return f"{manager_data['player_first_name']} {manager_data['player_last_name']}"

# Returns manager's region
def get_manager_country(manger_data):
    return manger_data['player_region_name']

def get_manager_team_name(manager_data):
    return manager_data['name']
       