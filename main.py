# Manually input scrim result
matches = [ 
    { 
        "date": "2026-02-06", 
        "opponent": "swaglord9000", 
        "match_type": "scrim", 
        "map": "Bind", 
        "result": "win", 
        "team_score": 16, 
        "enemy_score": 8, 
        "players": [ 
            
            { 
            "name": "Gek", 
            "agent": "Raze", 
            "kills": 27, 
            "deaths": 19, "assists": 7, 
            "ACS": 335, 
            "first_bloods": 6 
            }, 
            
            { 
            "name": "Josh", 
            "agent": "Brimstone", 
            "kills": 26, 
            "deaths": 14, 
            "assists": 5, 
            "ACS": 261, 
            "first_bloods": 1 
            }, 
            
            { 
            "name": "Jono", 
            "agent": "Viper", 
            "kills": 16, 
            "deaths": 19, 
            "assists": 6, 
            "ACS": 221, 
            "first_bloods": 5 
            }, 
            
            { 
            "name": "Jamie", 
            "agent": "Yoru", 
            "kills": 15, 
            "deaths": 12, 
            "assists": 3, 
            "ACS": 178, 
            "first_bloods": 2 
            }, 
            
            { 
            "name": "Walli", 
            "agent": "Fade", 
            "kills": 13, 
            "deaths": 13, 
            "assists": 6, 
            "ACS": 132, 
            "first_bloods": 1 
            }
        ] 
    },
    { 
        "date": "2026-02-06", 
        "opponent": "swaglord9000", 
        "match_type": "scrim", 
        "map": "Haven", 
        "result": "loss", 
        "team_score": 16, 
        "enemy_score": 8, 
        "players": [ 
            
            { 
            "name": "Gek", 
            "agent": "Raze", 
            "kills": 27, 
            "deaths": 19, "assists": 7, 
            "ACS": 335, 
            "first_bloods": 6 
            }, 
            
            { 
            "name": "Josh", 
            "agent": "Brimstone", 
            "kills": 26, 
            "deaths": 14, 
            "assists": 5, 
            "ACS": 261, 
            "first_bloods": 1 
            }, 
            
            { 
            "name": "Jono", 
            "agent": "Viper", 
            "kills": 16, 
            "deaths": 19, 
            "assists": 6, 
            "ACS": 221, 
            "first_bloods": 5 
            }, 
            
            { 
            "name": "Jamie", 
            "agent": "Yoru", 
            "kills": 15, 
            "deaths": 12, 
            "assists": 3, 
            "ACS": 178, 
            "first_bloods": 2 
            }, 
            
            { 
            "name": "Walli", 
            "agent": "Fade", 
            "kills": 13, 
            "deaths": 13, 
            "assists": 6, 
            "ACS": 132, 
            "first_bloods": 1 
            }
        ] 
    }
] 

# Funtion to calculate win rate (win rate = wins / total matches)
def calculate_win_rate(matches):
    total_matches = len(matches)
    wins = 0

    for match in matches:
        if match["result"] == "win":
            wins += 1

    if total_matches == 0:
        return 0

    return wins / total_matches

# Print win rate
win_rate = calculate_win_rate(matches)
print("Win rate:", win_rate)

# Function to calculate win rate by map
def calculate_win_rate_by_map(matches):
    map_stats = {}

    for match in matches:
        map_name = match["map"]

        # Create an entry for new map names (groups maps)
        if map_name not in map_stats:
            map_stats[map_name] = {
                "wins": 0,
                "total": 0
            }

        # Increments every time we see the same map (eg. increment for each Bind game)
        map_stats[map_name]["total"] += 1

        # Increment for win rate
        if match["result"] == "win":
            map_stats[map_name]["wins"] += 1

    # Calculate win rate per map
    for map_name in map_stats:
        wins = map_stats[map_name]["wins"]
        total = map_stats[map_name]["total"]
        map_stats[map_name]["win_rate"] = wins / total

    return map_stats

# Print win rate by map
map_win_rates = calculate_win_rate_by_map(matches)
print("Win rate by map:", map_win_rates)