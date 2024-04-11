from game_details import list_of_dict_of_games
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

# Extract ARI and Team 2 stats from the list of dictionaries
ARI_stats = [game['ARI'] for game in list_of_dict_of_games]
Team2_stats = [game['Team 2'] for game in list_of_dict_of_games]
scores = [game['Result'] for game in list_of_dict_of_games]

# Concatenate ARI_stats and Team2_stats at each corresponding position
concatenated_stats = [ari + team2 for ari, team2 in zip(ARI_stats, Team2_stats)]

# Split the data into training and testing sets
train_size = int(0.8 * len(concatenated_stats))
train_concatenated_stats = concatenated_stats[:train_size]
train_scores = scores[:train_size]
test_concatenated_stats = concatenated_stats[train_size:]
test_scores = scores[train_size:]

# Preprocess the data
train_concatenated_stats = np.array(train_concatenated_stats)
train_scores = np.array(train_scores)
test_concatenated_stats = np.array(test_concatenated_stats)
test_scores = np.array(test_scores)

# Normalize the input data
train_concatenated_stats = (train_concatenated_stats - np.mean(train_concatenated_stats)) / np.std(train_concatenated_stats)
test_concatenated_stats = (test_concatenated_stats - np.mean(test_concatenated_stats)) / np.std(test_concatenated_stats)

# Convert the target scores to a suitable format for training
train_scores = np.array([np.array(score) for score in train_scores])
test_scores = np.array([np.array(score) for score in test_scores])

# Build the model
model = Sequential()
model.add(Conv1D(filters=32, kernel_size=3, activation='relu', input_shape=(train_concatenated_stats.shape[1], 1)))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(2))  # Output layer with 2 units for score tuple

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(x=train_concatenated_stats, y=train_scores, epochs=10000, batch_size=64)

# Evaluate the model
test_loss = model.evaluate(x=test_concatenated_stats, y=test_scores)

# Test the model 
output = model.predict(test_concatenated_stats)
print(output)

# Save the model
model.save('data/model.h5')