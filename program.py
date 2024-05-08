from game import Game
import PySimpleGUI as sg  
from team import batting_order_dict as pod
from game_NN import NN_run
#keep the formating of (away_score, home_score) for storing the scores easily

def run_sim(away_team, home_team, iters=100):
    '''runs a simulation of a baseball game'''
    list_of_scores=[]
    avg_away_score=0
    avg_home_score=0
    
    for i in range(iters):
        g=Game(away_team, home_team)
        score, transcript=g.play_ball()
        list_of_scores.append(score)
        avg_away_score+=score[0]
        avg_home_score+=score[1]
    avg_away_score=avg_away_score/iters
    avg_home_score=avg_home_score/iters
    return avg_away_score, avg_home_score
    

def main():
    sg.theme('DarkGreen')
    sg.popup_auto_close("Welcome to the Baseball Simulator", auto_close_duration=2, button_type=sg.POPUP_BUTTONS_NO_BUTTONS, no_titlebar=True)
    
    team_keys=sorted(list(pod.keys()))
    layout = [
        [
            sg.Text("Welcome to the Baseball Simulator", font=('Arial', 20))
        ],
        [
            sg.Text("Away Team", key='away_title'), sg.Combo(team_keys, key='away_team')
        ],
        
        [
            sg.Text("Home Team", key='home_title'), sg.Combo(team_keys, key='home_team'),
        ],
        
        [
            sg.Button("Run Simulation", key='run_sim')
        ],
        [
            sg.Text("Simulation Results", font=('Arial', 15))
        ],

        [
            sg.Text("Estimated Score (simulator)", key='est_score'), sg.Text('Estimated Winner', key='est_winner'),
        ],
        [
            sg.Text("--------------------------------------------------")
        ],
        [
            sg.Text("Neural Network Predictions", font=('Arial', 15))
        ],
        [
            sg.Text("Predicted Score (NN)", key='nn_score'), sg.Text('Predicted Winner', key='pred_winner')
        ],
        [
            sg.ProgressBar(1, orientation='h', size=(20, 20), key='nn_confidence')
        ]

    ]
    window=sg.Window(title="Baseball Simulator", layout=layout, margins=(100, 100), font=('Arial', 13))
    while True:
        event, values=window.read()
        if event==sg.WIN_CLOSED:
            break
        if event=='run_sim':
            away_team=values['away_team']
            home_team=values['home_team']
            away_score, home_score=run_sim(away_team, home_team)
            window['est_score'].update(f'{away_score} - {home_score}')
            if away_score>home_score:
                window['est_winner'].update(f'{away_team} Wins')
            else:
                window['est_winner'].update(f'{home_team} Wins')
            nn_score, pred_winner, NN_confidence=NN_run(away_team, home_team)
            window['nn_score'].update(f'{nn_score[0][0]} - {nn_score[0][1]}')
            window['pred_winner'].update(pred_winner)
            window['nn_confidence'].update_bar(max(NN_confidence[0]))
        
            

if __name__ == "__main__":
    main()