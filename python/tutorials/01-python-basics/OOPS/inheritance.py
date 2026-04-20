import datetime

class Player:

    def __init__(self,first_name,last_name,birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def get_age(self):
        curr_year  = datetime.datetime.now().year
        return curr_year - self.birth_year

class Tennis(Player):
    
    def __init__(self,first_name,last_name,birth_year):
        super().__init__(first_name,last_name,birth_year)
        self.aces = []

    def get_avg_aces(self):
        return sum(self.aces)/len(self.aces)

    def get_aces(self,aces):
        self.aces.append(aces)
        
class Cricket(Player):
    
    def __init__(self,first_name,last_name,birth_year):
        super().__init__(first_name,last_name,birth_year)
        self.score = []
        
    def get_score(self,score):
        self.score.append(score)

    def get_avg_score(self):
        return sum(self.score)/len(self.score)


roger = Tennis("Roger","Dowry",1980)
roger.get_aces(34)
roger.get_aces(45)
roger.get_aces(67)
print(roger.aces)

virat = Cricket("Virat","Kohli",1988)
virat.get_score(45)
virat.get_score(2)
virat.get_score(100)

