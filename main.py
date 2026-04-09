# Manually input scrim result
matches = [ 
    { 
        "date": "06-02-2026", 
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
            "kills": 27, "deaths": 19, "assists": 7, 
            "ACS": 335, 
            "first_bloods": 6 
            }, 
            
            { 
            "name": "Josh", 
            "agent": "Brimstone", 
            "kills": 26, "deaths": 14, "assists": 5, 
            "ACS": 261, 
            "first_bloods": 1 
            }, 
            
            { 
            "name": "Jono", 
            "agent": "Viper", 
            "kills": 16, "deaths": 19, "assists": 6, 
            "ACS": 221, 
            "first_bloods": 5 
            }, 
            
            { 
            "name": "Jamie", 
            "agent": "Yoru", 
            "kills": 15, "deaths": 12, "assists": 3, 
            "ACS": 178, 
            "first_bloods": 2 
            }, 
            
            { 
            "name": "Walli", 
            "agent": "Fade", 
            "kills": 13, "deaths": 13, "assists": 6, 
            "ACS": 132, 
            "first_bloods": 1 
            }
        ] 
    },
    { 
        "date": "06-02-2026", 
        "opponent": "swaglord9000", 
        "match_type": "scrim", 
        "map": "Haven", 
        "result": "win", 
        "team_score": 14, 
        "enemy_score": 10, 
        "players": [ 
            
            { 
            "name": "Gek", 
            "agent": "Neon", 
            "kills": 24, "deaths": 20, "assists": 3, 
            "ACS": 297, 
            "first_bloods": 4
            }, 
            
            { 
            "name": "Josh", 
            "agent": "Omen", 
            "kills": 23, "deaths": 14, "assists": 5, 
            "ACS": 258, 
            "first_bloods": 1
            }, 
            
            { 
            "name": "Jono", 
            "agent": "Killjoy", 
            "kills": 23, "deaths": 13, "assists": 4, 
            "ACS": 260, 
            "first_bloods": 0
            }, 
            
            { 
            "name": "Jamie", 
            "agent": "Yoru", 
            "kills": 17, "deaths": 17, "assists": 6, 
            "ACS": 204, 
            "first_bloods": 6 
            }, 
            
            { 
            "name": "Walli", 
            "agent": "Fade", 
            "kills": 8, "deaths": 18, "assists": 4, 
            "ACS": 98, 
            "first_bloods": 3
            }
        ] 
    },
    { 
        "date": "04-02-2026", 
        "opponent": "KOR", 
        "match_type": "scrim", 
        "map": "Corrode", 
        "result": "win", 
        "team_score": 15, 
        "enemy_score": 9, 
        "players": [ 
            
            { 
            "name": "Gek", 
            "agent": "Waylay", 
            "kills": 22, "deaths": 15, "assists": 5, 
            "ACS": 246, 
            "first_bloods": 6
            }, 
            
            { 
            "name": "Josh", 
            "agent": "Viper", 
            "kills": 17, "deaths": 13, "assists": 3, 
            "ACS": 180, 
            "first_bloods": 0
            }, 
            
            { 
            "name": "Jono", 
            "agent": "Clove", 
            "kills": 20, "deaths": 18, "assists": 11, 
            "ACS": 263, 
            "first_bloods": 3
            }, 
            
            { 
            "name": "Jamie", 
            "agent": "Fade", 
            "kills": 20, "deaths": 12, "assists": 8, 
            "ACS": 215, 
            "first_bloods": 2
            }, 
            
            { 
            "name": "Walli", 
            "agent": "Yoru", 
            "kills": 15, "deaths": 14, "assists": 5, 
            "ACS": 188, 
            "first_bloods": 1
            }
        ] 
    },
    { 
        "date": "04-02-2026", 
        "opponent": "KOR", 
        "match_type": "scrim", 
        "map": "Bind", 
        "result": "loss", 
        "team_score": 9, 
        "enemy_score": 15, 
        "players": [ 
            
            { 
            "name": "Gek", 
            "agent": "Waylay", 
            "kills": 22, "deaths": 19, "assists": 2, 
            "ACS": 238, 
            "first_bloods": 4
            }, 
            
            { 
            "name": "Josh", 
            "agent": "Brimstone", 
            "kills": 13, "deaths": 17, "assists": 10, 
            "ACS": 149, 
            "first_bloods": 1
            }, 
            
            { 
            "name": "Jono", 
            "agent": "Viper", 
            "kills": 24, "deaths": 16, "assists": 4, 
            "ACS": 291, 
            "first_bloods": 3
            }, 
            
            { 
            "name": "Jamie", 
            "agent": "Skye", 
            "kills": 14, "deaths": 19, "assists": 10, 
            "ACS": 204, 
            "first_bloods": 2
            }, 
            
            { 
            "name": "Walli", 
            "agent": "Tejo", 
            "kills": 9, "deaths": 16, "assists": 5, 
            "ACS": 129, 
            "first_bloods": 3
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



# Function to calculate win rate by map
def calculate_win_rate_by_map(matches):
    map_stats = {}

    for match in matches:
        map_name = match["map"]

        # Create an entry for new map names (group maps)
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

# Stores function result
map_win_rates = calculate_win_rate_by_map(matches)

# Print overall win rate
win_rate = calculate_win_rate(matches)
print("Win rate:", win_rate)

# Print win rate by map
print("\nWin rate by map:")
for map_name, stats in map_win_rates.items():
    print(f"{map_name}: {stats['wins']} wins out of {stats['total']} matches ({stats['win_rate']:.0%})")