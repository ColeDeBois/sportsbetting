from game_details import list_of_dict_of_games
import tensorflow as tf
import numpy as np
import pandas as pd
def NN_run(away, home):
# Load the model
    model =  tf.keras.models.load_model('data/model.h5')

    # Extract SEA Stats
    batters= pd.read_csv('data/mlb-player-stats-Batters.csv')
    pitchers= pd.read_csv('data/mlb-player-stats-P.csv')
    # home = "ARI"
    # away = "SEA"

    # Concatenate stats
    # ARI_stats = list_of_dict_of_games[0]['ARI'][:990] # these numbers have to be in place for it to work as how i trained the model :3
    Home_stats = [batters[(batters['Team'] == home)].drop(columns=batters.columns[:3]), pitchers[(pitchers['Team'] == home)].drop(columns=pitchers.columns[:3])]
    Home_stats = [stat for stats in Home_stats for stat in stats.values.flatten()][:990]
    Away_stats = [batters[(batters['Team'] == away)].drop(columns=batters.columns[:3]), pitchers[(pitchers['Team'] == away)].drop(columns=pitchers.columns[:3])]
    Away_stats = [stat for stats in Away_stats for stat in stats.values.flatten()][:754]
    concatenated_stats = Home_stats + Away_stats

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
            winner = home + " Wins!"
        elif team2_score > team1_score:
            winner = away + " Wins!"
        else:
            winner = "Tie"
        
        confidence_scores = np.exp(predicted_scores) / np.sum(np.exp(predicted_scores))
        return predicted_scores, winner, confidence_scores

    return run_model(concatenated_stats)
    # Example usage
    output = run_model(concatenated_stats)
    print(output)
