from team import Team, batting_order_dict, pitcher_order_dict
import pandas as pd
import random


class Game:
    def __init__(self, home_team, away_team) -> None:
        df_bat=pd.read_csv('data/mlb-player-stats-Batters.csv')
        df_pit=pd.read_csv('data/mlb-player-stats-P.csv')
        self.homeT=Team(home_team, df_bat, df_pit, batting_order_dict[home_team], pitcher_order_dict[home_team])
        self.awayT=Team(away_team, df_bat, df_pit, batting_order_dict[away_team], pitcher_order_dict[away_team])
        
        self.inning=0
        self.home_runs=0
        self.away_runs=0
        self.bases=[]

    def clear_bases(self):
        self.bases=[None, None, None]

    def advance_runners(self, num_bases, new_batter, team_runs):
        for i in range(num_bases):
            if self.bases[2]!=None:
                self.bases[2]=None
                if str(self.homeT.name)==new_batter.team:
                    self.home_runs+=1
                else:
                    self.away_runs+=1
            if self.bases[1]!=None:
                self.bases[2]=self.bases[1]
                self.bases[1]=None
            if self.bases[0]!=None:
                self.bases[1]=self.bases[0]
                self.bases[0]=None
            if i==0:
                self.bases[0]=new_batter
        
        

    def play_ball(self):
        while self.inning<=9:
            self.inning+=1
            self.play_inning()
        print('Game Over')
        print(f'{self.awayT}: {self.away_runs} {self.homeT}: {self.home_runs}')

    def play_inning(self):
        print(f"It's the top of the {self.inning}th inning")
        print(f"The Score is {self.awayT}: {self.away_runs} {self.homeT}: {self.home_runs}")
        outs=0

        #away team at bat
        self.clear_bases()
        while outs<3:
            batter=self.awayT.at_bat
            pitcher=self.homeT.pitcher
            result=self.play_at_bat(batter, pitcher)
            if result=='OUT':
                outs+=1
                print(f'{batter} strikes out, {outs} outs')
            else:
                self.advance_runners(result, batter, self.away_runs)
                print(f'{batter} gets a {result} base hit')
            self.awayT.batter_up()
            print(f'bases: {self.bases}','\n')
        #home team at bat
        self.clear_bases()
        while outs<6 and outs>=3:
            batter=self.homeT.at_bat
            pitcher=self.awayT.pitcher
            result=self.play_at_bat(batter, pitcher)   
            if result=='OUT':
                outs+=1
                print(f'{batter} strikes out, {outs % 3} outs')
            else:
                self.advance_runners(result, batter, self.home_runs)
                print(f'{batter} gets a {result} base hit')
            print(f'bases: {self.bases}', '\n')
            self.homeT.batter_up()


    

    def play_at_bat(self, batter, pitcher):
        '''plays an at bat, returns the number of bases the batter advanced'''
        hit_prob=(batter.hit_prob + pitcher.hit_prob)/2
        walk_prob=(batter.walk_prob + pitcher.walk_prob)/2
        chance=random.random()
        if walk_prob>chance:
            return 1
        if hit_prob>chance:
            probabilities=batter.probs
            probabilities[3]=(probabilities[3]+pitcher.hr_prob)/2
            bases_hit=random.choices([1, 2, 3, 4], probabilities)
            return bases_hit[0]
        else:
            return 'OUT'
            
            
            
    def __str__(self) -> str:
        return f'{self.awayT} vs {self.homeT}'
    def __repr__(self) -> str:  
        return self.__str__()

