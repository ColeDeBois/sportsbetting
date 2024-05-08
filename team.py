#initial thoughts behind accessing player info
batting_order_dict={
    'LAD': ['Mookie Betts', 'Freddie Freeman', 'J.D. Martinez', 'Max Muncy', 'Will Smith', 'Jason Heyward', 'Enrique Hernandez', 'David Peralta', 'Miguel Rojas'],
    'LAA': ['Nolan Schanuel', 'Shohei Ohtani', 'Brandon Drury', 'Mike Moustakas', 'Luis Rengifo', 'Mickey Moniak', 'Logan O\'Hoppe', 'Trey Cabbage', 'Randal Grichuk'],
    'ARI': ['Ketel Marte', 'Corbin Carroll', 'Lourdes Gurriel', 'Christian Walker', 'Evan Longoria', 'Pavin Smith', 'Nick Ahmed', 'Gabriel Moreno', 'Jake McCarthy'],
    'SEA': ['J.P. Crawford', 'Ty France', 'Julio Rodriguez', 'Jarred Kelenic', 'Eugenio Suarez', 'Teoscar Hernandez', 'Taylor Trammell', 'Tom Murphy', 'Jose Caballero'],
   'TEX':['Marcus Semien','Corey Seager','Nathaniel Lowe','Adolis Garcia','Josh Jung','Jonah Heim','Robbie Grossman','Ezequiel Duran','Leody Taveras'],
   'OAK':['Esteury Ruiz','Ramon Laureano','Ryan Noda','Brent Rooker','Jonah Bride','Carlos Perez','Aledmys Diaz','Jace Peterson','Shea Langeliers'],
   'DET':['Matt Vierling','Spencer Torkelson','Kerry Carpenter','Javier Baez','Nick Maton','Nick Maton','Miguel Cabrera','Jake Rogers','Jake Marisnick' ],
   'CLE':['Steven Kwan','Amed Rosario','Jose Ramirez','Josh Naylor','Josh Bell','Andres Gimenez','Myles Straw','Will Brennan','Cam Gallagher'],
   'CIN':['TJ Friedl','Matt McLain','Jonathan India','Elly De La Cruz','Spencer Steer','Tyler Stephenson','Will Benson','Nick Senzel','Curt Casali'],
   'PIT':['Andrew McCutchen','Bryan Reynolds','Connor Joe','Carlos Santana','Ke\'Bryan Hayes','Rodolfo Castro','Ji Hwan Bae','Mark Mathias','Austin Hedges'],
   'TOR':['George Springer','Whit Merrifield','Bo Bichette','Vladimir Guerrero','Daulton Varsho','Matt Chapman','Danny Jansen','Cavan Biggio','Kevin Kiermaier'],
   'PHI':['Kyle Schwarber','Trea Turner','Alec Bohm','Bryce Harper','J.T. Realmuto','Bryson Stott','Kody Clemens','Brandon Marsh','Edmundo Sosa'],
   'BAL':['Austin Hays','Adley Rutschman','Anthony Santander','Gunnar Henderson','Ramon Urias','Aaron Hicks','James McCann','Jorge Mateo','Joey Ortiz'],
   'WAS':['Lane Thomas','Luis Garcia','Jeimer Candelario','Joey Meneses','Stone Garrett','Dominic Smith','Riley Adams','Victor Robles','CJ Abrams'],
   'CWS':['Andrew Benintendi','Tim Anderson','Luis Robert','Eloy Jimenez','Gavin Sheets','Andrew Vaughn','Jake Burger','Elvis Andrus','Seby Zavala'],
   'TB':['Yandy Diaz','Wander Franco','Harold Ramirez','Randy Arozarena','Isaac Paredes','Taylor Walls','Manuel Margot','Francisco Mejia','Jose Siri'],
   'HOU':['Corey Julks','Jose Altuve','Kyle Tucker','Alex Bregman','Jose Abreu','Yainer Diaz','Jeremy Pena','Jake Meyers','Grae Kessinger'],
   'ATL':['Mickey Moniak','Shohei Ohtani','Mike Trout','Brandon Drury','Matt Thaiss','Taylor Ward','Michael Stefanic','Luis Rengifo','Andrew Velazquez'],
   'SD':['Fernando Tatis','Juan Soto','Manny Machado','Xander Bogaerts','Jake Cronenworth','Gary Sanchez','Matt Carpenter','Ha-Seong Kim','Trent Grisham'],
   'CHC':['LaMonte Wade','Joc Pederson','Thairo Estrada','Michael Conforto','Mike Yastrzemski','Luis Matos','Patrick Bailey','Brandon Crawford','Casey Schmitt'],
   'MIN':['Byron Buxton','Donovan Solano','Carlos Correa','Kyle Farmer','Royce Lewis','Willi Castro','Alex Kirilloff','Ryan Jeffers','Michael A. Taylor'],
   'MIL':['Christian Yelich','Jesse Winker','Willy Adames','Rowdy Tellez','Luis Urias','Raimel Tapia','Brian Anderson','Victor Caratini','Joey Wiemer'],
   'KC':['Nick Pratto','Bobby Witt','Salvador Perez','MJ Melendez','Edward Olivares','Maikel Garcia','Nicky Lopez','Samad Taylor','Drew Waters'],
   'NYM':['Brandon Nimmo','Starling Marte','Jeff McNeil','Tommy Pham','Brett Baty','Francisco Alvarez','Daniel Vogelbach','Mark Canha','Luis Guillorme'],
   'STL':['Brendan Donovan','Paul Goldschmidt','Nolan Arenado','Willson Contreras','Jordan Walker','Nolan Gorman','Paul DeJong','Tommy Edman','Alec Burleson'],
   'SF':['LaMonte Wade','Joc Pederson','Thairo Estrada','Michael Conforto','Mike Yastrzemski','Luis Matos','Patrick Bailey','Brandon Crawford','Casey Schmitt'],
   'COL':['Jurickson Profar','Ezequiel Tovar','Ryan McMahon','Elias Diaz','Randal Grichuk','Harold Castro','Elehuris Montero','Brenton Doyle','Austin Wynns' ],
   'MIA':['Jorge Soler','Luis Arraez','Bryan De La Cruz','Garrett Cooper','Jesús Sanchez','Joey Wendle','Jonathan Davis','Nick Fortes','Garrett Hampson'],
   'NYY':['Jake Bauers','Gleyber Torres','Anthony Rizzo','Giancarlo Stanton','Josh Donaldson','Billy McKinney','Oswaldo Cabrera','Kyle Higashioka','Anthony Volpe'],
   'BOS':['Jarren Duran','Justin Turner','Alex Verdugo','Rafael Devers','Rob Refsnyder','Triston Casas','Enrique Hernandez','Reese McGuire','Pablo Reyes'],
        }
pitcher_order_dict={
    'LAA': ['Reid Detmers'],
    'LAD': ['Lance Lynn'],
    'ARI': ['Zac Gallen'],
    'SEA': ['Luis Castillo'],
   'TEX':['Jacob deGrom'],
   'OAK':['Kyle Muller'],
   'DET':['Eduardo Rodriguez'],
   'CLE':['Shane Bieber'],
   'CIN':['Hunter Greene'],
   'PIT':['Mitch Keller'],
   'TOR':['Alek Manoah'],
   'PHI':['Aaron Nola'],
   'BAL':['Kyle Gibson'],
   'WAS':['Patrick Corbin'],
   'CWS':['Dylan Cease'],
   'TB':['Shane McClanahan'],
   'HOU':['Framber Valdez'],
   'ATL':['Max Fried'],
   'SD':['Yu Darvish'],
   'CHC':['Marcus Stroman'],
   'MIN':['Pablo López'],
   'MIL':['Corbin Burnes'],
   'KC':['Zack Greinke'],
   'NYM':['Max Scherzer'],
   'STL':['Miles Mikolas'],
   'SF':['Logan Webb'],
   'COL':['German Marquez'],
   'MIA':['Sandy Alcantara'],
   'NYY':['Gerrit Cole'],
   'BOS':['Chris Sale'],
    }
class Batter:
    def __init__(self, name, df, team) -> None:
        df=df[df['Player']==name]
        self._df=df
        self._name=name
        self._team=team
    def __str__(self) -> str:
        return str(self.team)+' '+self._name
    def __repr__(self) -> str:
        return self.__str__()
    @property
    def team(self):
        return self._team
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
        try:
            value = self._df['H'].iloc[0]/self._df['AB'].iloc[0]
        except:
            print(self._name)
        return value
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
        # df_bat=df_bat[df_bat['Team']==name]
        for b in batting_order:
            b=Batter(b, df_bat, name)
            self.batters.append(b)
        
        self.pitchers=[]
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
        

