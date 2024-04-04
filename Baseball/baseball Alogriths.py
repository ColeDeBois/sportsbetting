import random
import time
#figure out how to get runners off if once inning reset
players = [
    {"name": "Tasso Foster", "single": 0.272, "double": 0.072, "triple": 0.001, "homerun": 0.001, "out": 0.654,"walk":0.154},
    {"name": "Rocco Granucci", "single": 0.203, "double": 0.09, "triple": 0.001, "homerun": 0.055, "out": 0.651,"walk":0.151},
    {"name": "Carl Lawson", "single": 0.37, "double": 0.001, "triple": 0.001, "homerun": 0.037, "out": 0.591,"walk":0.120},
    {"name": "Drew Baskin", "single": 0.150, "double": 0.095, "triple": 0.027, "homerun": 0.041, "out": 0.605,"walk":0.082},
    {"name": "Luke Piazza", "single": 0.224, "double": 0.052, "triple": 0.001, "homerun": 0.034, "out": 0.431,"walk":0.120},
    {"name": "Jeff Hoffman", "single": 0.246, "double": 0.035, "triple": 0.018, "homerun": 0.105, "out": 0.369,"walk":0.227},
    {"name": "Clint Walker", "single": 0.25, "double": 0.089, "triple": 0.018, "homerun": 0.053, "out": 0.3576,"walk":0.232},
    {"name": "Carter Stoltz", "single": 0.162, "double": 0.046, "triple": 0.001, "homerun": 0.047, "out": 0.535,"walk":0.209},
    {"name": "Jason Smith", "single": 0.001, "double": 0.001, "triple": 0.001, "homerun": 0.500, "out": 0.247,"walk":0.250},
    """{"name": "Liam O'Conner", "single": 0.171, "double": 0.085, "triple": 0.001, "homerun": 0.001, "out": 0.628,"walk":0.114},
    {"name": "Layton Wagner", "single": 0.142, "double": 0.114, "triple": 0.001, "homerun": 0.001, "out": 0.561,"walk":0.114},
    {"name": "Adam Birt", "single": 0.290, "double": 0.032, "triple": 0.001, "homerun": 0.001, "out": 0.580,"walk":0.096},
    {"name": "Wyatt Thames", "single": 0.240, "double": 0.001, "triple": 0.001, "homerun": 0.04, "out": 0.673,"walk":0.096},
    {"name": "Caden Davis", "single": 0.095, "double": 0.095, "triple": 0.001, "homerun": 0.001, "out": 0.618,"walk":0.190},
    {"name": "Charlie Ferbet", "single": 0.200, "double": 0.050, "triple": 0.050, "homerun": 0.001, "out": 0.321,"walk":0.020},
    {"name": "Nate Hamburger", "single": 0.143, "double": 0.071, "triple": 0.001, "homerun": 0.001, "out": 0.641,"walk":0.143},
    {"name": "Jackson Garrett", "single": 0.090, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.726,"walk":0.181},
    {"name": "Nick Arnett", "single": 0.200, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.757,"walk":0.040},
    {"name": "Boone Rush", "single": 0.400, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.397,"walk":0.200},
    {"name": "Cody Guy", "single": 0.001, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.796,"walk":0.200},
    {"name": "Preston Lau", "single": 0.001, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.995,"walk":0.001},
    {"name": "Micah Ayala", "single": 0.001, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.995,"walk":0.001},
    {"name": "Finn Hoover", "single": 0.001, "double": 0.0010, "triple": 0.001, "homerun": 0.001, "out": 0.995,"walk":0.001},
    {"name": "Charlie Satterlee", "single": 0.250, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.746,"walk":0.001},
    {"name": "Joshua Murphy", "single": 0.001, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.995,"walk":0.001},"""

]   


away_players=[
    {"name": "Liam O'Conner", "single": 0.171, "double": 0.085, "triple": 0.001, "homerun": 0.001, "out": 0.628,"walk":0.114},
    {"name": "Layton Wagner", "single": 0.142, "double": 0.114, "triple": 0.001, "homerun": 0.001, "out": 0.561,"walk":0.114},
    {"name": "Adam Birt", "single": 0.290, "double": 0.032, "triple": 0.001, "homerun": 0.001, "out": 0.580,"walk":0.096},
    {"name": "Wyatt Thames", "single": 0.240, "double": 0.001, "triple": 0.001, "homerun": 0.04, "out": 0.673,"walk":0.096},
    {"name": "Caden Davis", "single": 0.095, "double": 0.095, "triple": 0.001, "homerun": 0.001, "out": 0.618,"walk":0.190},
    {"name": "Charlie Ferbet", "single": 0.200, "double": 0.050, "triple": 0.050, "homerun": 0.001, "out": 0.321,"walk":0.020},
    {"name": "Nate Hamburger", "single": 0.143, "double": 0.071, "triple": 0.001, "homerun": 0.001, "out": 0.641,"walk":0.143},
    {"name": "Jackson Garrett", "single": 0.090, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.726,"walk":0.181},
    {"name": "Nick Arnett", "single": 0.200, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.757,"walk":0.040},
    {"name": "Boone Rush", "single": 0.400, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.397,"walk":0.200},
    {"name": "Cody Guy", "single": 0.001, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.796,"walk":0.200},
    {"name": "Preston Lau", "single": 0.001, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.995,"walk":0.001},
    {"name": "Micah Ayala", "single": 0.001, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.994,"walk":0.001},
    {"name": "Finn Hoover", "single": 0.001, "double": 0.0010, "triple": 0.001, "homerun": 0.001, "out": 0.995,"walk":0.001},
    {"name": "Charlie Satterlee", "single": 0.250, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.746,"walk":0.001},
    {"name": "Joshua Murphy", "single": 0.001, "double": 0.001, "triple": 0.001, "homerun": 0.001, "out": 0.995,"walk":0.001},

] 
home_score = 0
away_score = 0
outs = 0
half_inning = 1
current_player_index = 0
base_runners = [0, 0, 0, 0]

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
    
    if outs == 3:
        switch_half_inning()




def switch_half_inning():
    global half_inning
    global outs
    global home_score
    global away_score
    global base_runners  # Add global declaration for base_runners
    print("\nThree outs! Switching sides.")
    #time. sleep(2)
    outs = 0
    base_runners = [0, 0, 0, 0]  # Reset base runners to empty bases
    half_inning += 1
    print("\nScoreboard:")
    print(f"Home: {home_score} - Away: {away_score}")
    if half_inning > 9 or (half_inning == 9 and home_score != away_score):
        print("Game over!")
        return
    print("\nStarting the next half inning.") 



def base_runner(result):
    global home_score
    global away_score
    global base_runners
    if result in ["single", "double", "triple", "homerun", "walk"]:
        if result == "single":
            #if base_runners != [0, 0, 0, 0]:
                base_runners = [1] + base_runners[:-1]
        elif result =="walk":
            base_runners = [1] + base_runners[:-1]
        elif result == "double":
            #if base_runners != [0, 0, 0, 0]:
                base_runners = [0, 1] + base_runners[:-2]
        elif result == "triple":
            #if base_runners != [0, 0, 0, 0]:
                base_runners = [0, 0, 1] + base_runners[:-3]
        elif result == "homerun":
            base_runners = [0, 0, 0, 1]
        for i in range(min(3, len(base_runners))):
            if base_runners[i] == 1:
                if half_inning % 2 == 0:
                    home_score += 1
                else:
                    away_score+=1
                
    runners = base_runners[:3]
    if runners == [1, 0, 0]:
        print(f"1B: X  2B:   3B:   \n")
    elif runners == [0, 1, 0]:
        print(f"1B:    2B: X  3B:   \n")
    elif runners == [0, 0, 1]:
        print(f"1B:    2B:   3B: X \n")
    elif runners == [1, 1, 0]:
        print(f"1B: X  2B: X  3B:   \n")
    elif runners == [1, 0, 1]:
        print(f"1B: X  2B:   3B: X \n")
    elif runners == [0, 1, 1]:
        print(f"1B:    2B: X  3B: X \n")
    elif runners == [1, 1, 1]:
        print(f"1B: X  2B: X  3B: X \n")
    #time. sleep(2)

def main():
    global half_inning
    global current_player_index
    global players
    global outs  
    print(f"\nInning {half_inning}")
    while half_inning <= 9:  
        if half_inning %2 == 0:
            for _ in range(len(players)):
                player = players[current_player_index]
                simulate_at_bat(player) 
                if outs == 3:
                    break  
                current_player_index = (current_player_index + 1) % len(players)
            current_player_index = 0
            if half_inning >= 9 and home_score != away_score:
                print("Game over!")
                break
        if half_inning % 2 != 0:
            for _ in range(len(away_players)):
                away_player = away_players[current_player_index]
                simulate_at_bat(away_player) 
                if outs == 3:
                    break  
                current_player_index = (current_player_index + 1) % len(away_players)
            current_player_index = 0
            
if __name__ == "__main__":
    main()