import random
players = [
    {"name": "Tasso Foster", "single": 0.272, "double": 0.072, "triple": 0.001, "homerun": 0.001, "out": 0.654,"walk":0.154},
    {"name": "Rocco Granucci", "single": 0.203, "double": 0.09, "triple": 0.001, "homerun": 0.055, "out": 0.651,"walk":0.151},
    {"name": "Carl Lawson", "single": 0.37, "double": 0.001, "triple": 0.001, "homerun": 0.037, "out": 0.591,"walk":0.120},
    
]
home_score = 0
away_score = 0
outs = 0
half_inning = 1
current_player_index = 0
base_runners = [0, 0, 0, 0, 0, 0, 0,0]

def fouts():
    global outs
    outcomes = ["single", "double", "triple", "homerun", "out","walk"]
    weights = [players[current_player_index][outcome] for outcome in outcomes]
    chosen_outcome = random.choices(outcomes, weights=weights, k=1)[0]
    if chosen_outcome == "out":
        outs += 1
    return chosen_outcome

def simulate_at_bat(player):
    global outs
    global current_player_index
    global players
    global base_runners
    print(f"{player['name']}'s turn at bat:")
    outcome = fouts()
    if outcome != "out":
        print(f"{player['name']} gets a {outcome}!")
        #time. sleep(2)
    else:
        print(f"{player['name']} is out!")
        #time. sleep(2)
    base_runner(outcome)  # Call base_runner function with the outcome, even if the player is out
    current_player_index = (current_player_index + 1) % len(players)
    





def base_runner(result):
    global home_score
    global away_score
    global base_runners
    if result in ["single", "double", "triple", "homerun", "walk"]:
        if result == "single":
            base_runners = [1] + base_runners[:-1]
            print (base_runners)
        elif result =="walk":
            base_runners = [1] + base_runners[:-1]
            print (base_runners)
        elif result == "double":
            base_runners = [0, 1] + base_runners[:-2]
            print (base_runners)
        elif result == "triple":
            base_runners = [0, 0, 1] + base_runners[:-3]
            print (base_runners)
        elif result == "homerun":
            base_runners = [0, 0, 0, 1]
            print (base_runners)
        
        if base_runners[3] == 1:
            home_score += 1
            print(home_score)
            base_runners[3] = 0 
        
        if base_runners[4] == 1:
            home_score += 1
            print(home_score)
            base_runners[4] = 0  # Corrected this line
        
        if base_runners[5] == 1:
            home_score += 1
            print(home_score)
            base_runners[5] = 0  # Corrected this line
        
        if base_runners[6] == 1:
            home_score += 1
            print(home_score)
            base_runners[6] = 0  # Corrected this line
        
        if base_runners[7] == 1:
            home_score += 1
            print(home_score)
            base_runners[7] = 0  # Corrected this line
        
    
                
        

    

def main():
    global half_inning
    global current_player_index
    global players
    global outs  
    print(f"\nInning {half_inning}")
    while half_inning <= 9:  
            for _ in range(len(players)):
                player = players[current_player_index]
                simulate_at_bat(player) 
                if outs == 3:
                    break  
                current_player_index = (current_player_index + 1) % len(players)
            current_player_index = 0
            

    


            
            
if __name__ == "__main__":
    main()