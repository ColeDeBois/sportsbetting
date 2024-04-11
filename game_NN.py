from game_details import list_of_dict_of_games
import tensorflow as tf
import numpy as np
import pandas as pd

# Load the model
model =  tf.keras.models.load_model('data/model.h5')

# Extract SEA Stats
batters= pd.read_csv('data/mlb-player-stats-Batters.csv')
pitchers= pd.read_csv('data/mlb-player-stats-P.csv')


# Concatenate stats
ARI_stats = list_of_dict_of_games[0]['ARI'][:990] # these numbers have to be in place for it to work as how i trained the model :3
# If you want to put in your own games use the commented out section below
# OTHER_stats = [batters[(batters['Team'] == "OTHER")].drop(columns=batters.columns[:3]), pitchers[(pitchers['Team'] == "OTHER")].drop(columns=pitchers.columns[:3])]
# OTHER_stats = [stat for stats in OTHER_stats for stat in stats.values.flatten()][:990]
SEA_stats = [batters[(batters['Team'] == "SEA")].drop(columns=batters.columns[:3]), pitchers[(pitchers['Team'] == "SEA")].drop(columns=pitchers.columns[:3])]
SEA_stats = [stat for stats in SEA_stats for stat in stats.values.flatten()][:754]
# Team2_stats = list_of_dict_of_games[0]['Team 2'] # this is the team COL, its kinda convoluted
concatenated_stats = ARI_stats + SEA_stats

def run_model(input_data):
    # Preprocess the input data
    input_data = np.array(input_data)
    input_data = (input_data - np.mean(input_data)) / np.std(input_data)
    input_data = input_data.flatten()[None, :]

    # Run the model and get the predicted scores
    predicted_scores = model.predict(input_data)
    predicted_scores = np.round(predicted_scores)  # Round the predicted scores
    
    # Determine the winner based on the scores
    team1_score = predicted_scores[0][0]
    team2_score = predicted_scores[0][1]
    if team1_score > team2_score:
        winner = "ARI Wins!"
    elif team2_score > team1_score:
        winner = "SEA Wins!"
    else:
        winner = "Tie"
    
    return predicted_scores, winner

# Example usage
output = run_model(concatenated_stats)
print(output)
