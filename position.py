# Determines position of player (event)
def determine_position(event_type):
    match event_type:
        case 1:
            return "GKP"
        case 2: 
            return "DEF" 
        case 3:
            return "MID"
        case 4: 
            return "FWD"