# Import necessary libraries
from pybaseball import schedule_and_record, pitching_stats, batting_stats
import pandas as pd

# Team abreviations & batters + pitchers
batters= pd.read_csv('data/mlb-player-stats-Batters.csv')
pitchers= pd.read_csv('data/mlb-player-stats-P.csv')
ARI = 'ARI'
# team2 = 'SEA'

# Get the schedule and results of games played by the teams in 2021
schedule_ari = schedule_and_record(2020, team=ARI)
# schedule_sea = schedule_and_record(2021, team=team2)

# schedule_ari.to_csv('schedule.txt', index=False)

# Create an empty list to store the game details
game_details = []

# Iterate over each game for SEA in the schedule 
def list_games():
    for index, game in schedule_ari.iterrows():
        # Get the game details
        game_result = (game['R'], game['RA'])
        team2 = game['Opp']

        # Get the player stats of the teams, also filter out any text in the array (needed for the NN model)
        sea_stats = [batters[(batters['Team'] == ARI)].drop(columns=batters.columns[:3]), pitchers[(pitchers['Team'] == ARI)].drop(columns=pitchers.columns[:3])]
        team2_stats = [batters[(batters['Team'] == team2)].drop(columns=batters.columns[:3]), pitchers[(pitchers['Team'] == team2)].drop(columns=pitchers.columns[:3])]
        
        # Flatten each stats into 1D arrays
        sea_stats = [stat for stats in sea_stats for stat in stats.values.flatten()]
        team2_stats = [stat for stats in team2_stats for stat in stats.values.flatten()]


        # Add the game details and player stats to the list
        game_details.append({
            'Result': game_result,
            'ARI': sea_stats,
            'Team 2': team2_stats
        })
    return game_details

# save dictionary into a text file
list_games()
with open('game_details.txt', 'w') as file:
    file.write(str(game_details))
