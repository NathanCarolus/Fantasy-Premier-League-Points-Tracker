import league
def get_active_leagues(manger_data):
    for active_phase in manger_data['active_phases']:
        league_name = league.get_league_name(active_phase['league_id'])
        print(f"{league_name}")
        
def get_manager_info(manger_data):
    return None
        