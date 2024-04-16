#initial thoughts behind accessing player info
batting_order_dict={
    'LAD': ['Mookie Betts', 'Freddie Freeman', 'J.D. Martinez', 'Max Muncy', 'Will Smith', 'Jason Heyward', 'Enrique Hernandez', 'David Peralta', 'Miguel Rojas'],
    'LAA': ['Nolan Schanuel', 'Shohei Ohtani', 'Brandon Drury', 'Mike Moustakas', 'Luis Rengifo', 'Mickey Moniak', 'Logan O\'Hoppe', 'Trey Cabbage', 'Randal Grichuk'],
    'ARI': ['Ketel Marte', 'Corbin Carroll', 'Lourdes Gurriel', 'Christian Walker', 'Evan Longoria', 'Pavin Smith', 'Nick Ahmed', 'Gabriel Moreno', 'Jake McCarthy'],
    'SEA': ['J.P. Crawford', 'Ty France', 'Julio Rodriguez', 'Jarred Kelenic', 'Eugenio Suarez', 'Teoscar Hernandez', 'Taylor Trammell', 'Tom Murphy', 'Jose Caballero'],
    'GOD': ['God', 'God', 'God', 'God', 'God', 'God', 'God', 'God', 'God']
}
pitcher_order_dict={
    'LAA': ['Reid Detmers'],
    'LAD': ['Lance Lynn'],
    'ARI': ['Zac Gallen'],
    'SEA': ['Luis Castillo'],
    'GOD': ['God']
}
class Batter:
    def __init__(self, name, df) -> None:
        df=df[df['Player']==name]
        self._df=df
        self._name=name
    def __str__(self) -> str:
        return str(self.team)+' '+self._name
    def __repr__(self) -> str:
        return self.__str__()
    @property
    def team(self):
        return self._df['Team'].iloc[0]
    @property
    def probs(self) -> list[float]:
        '''returns a list of probabilities for each at bat outcome in form of [single, 2b, 3b, hr]'''
        at_bats=(self._df['AB']).iloc[0]
        hit_2b=(self._df['2B']/at_bats).iloc[0]
        hit_3b=(self._df['3B']/at_bats).iloc[0]
        hit_hr=(self._df['HR']/at_bats).iloc[0]
        hit_single=((self._df['H']-self._df['2B']-self._df['3B']-self._df['HR'])/at_bats).iloc[0]
        
        probs=[hit_single, hit_2b, hit_3b, hit_hr]
        return probs
    @property
    def hit_prob(self) -> float:
        '''returns the probability of a hit '''
        return self._df['H'].iloc[0]/self._df['AB'].iloc[0]
    @property
    def walk_prob(self) -> float:
        '''returns the probability of a walk'''
        return (self._df['BB']/self._df['AB']).iloc[0]
    
class Pitcher:
    def __init__(self, name, df) -> None:
        self._df=df[df['Player']==name]
        self.name=name
    def __str__(self) -> str:
        return self.name
    def __repr__(self) -> str:
        return self.__str__()
    @property
    def hit_prob(self) -> float:
        '''returns a probability of a hit'''
        return (self._df['H']/(self._df['H']+self._df['K'])).iloc[0]
    @property
    def hr_prob(self) -> float:
        '''returns a probability of a home run'''
        batters_faced=self._df['H']+self._df['K']+self._df['BB']
        hit_hr=self._df['HR']/batters_faced
        return (hit_hr).iloc[0]
    @property
    def walk_prob(self) -> float:
        '''returns a probability of a walk'''
        batters_faced=self._df['H']+self._df['K']+self._df['BB']
        return (self._df['BB']/batters_faced).iloc[0]
        

class Team:
    def __init__(self, name, df_bat, df_pit, batting_order, pit_order) -> None:
        self.name=name
        self.batters=[]
        df_bat=df_bat[df_bat['Team']==name]
        for b in batting_order:
            b=Batter(b, df_bat)
            self.batters.append(b)
        
        self.pitchers=[]
        df_pit=df_pit[df_pit['Team']==name]
        for p in pit_order:
            p=Pitcher(p, df_pit)
            self.pitchers.append(p)
        self.bats=0
    def __str__(self) -> str:
        return self.name
    def __repr__(self) -> str:
        return self.__str__()
    
    @property
    def batting_order(self) -> list:
        '''returns the batting order of the team'''
        return self.batters
    @property
    def pitcher(self):
        '''returns the pitcher of the team'''
        return self.pitchers[0]
    @property
    def at_bat(self):
        '''returns the batter at the plate'''
        return self.batters[self.bats%9]
    def batter_up(self):
        '''cycles through the batting order'''
        self.bats+=1
        

