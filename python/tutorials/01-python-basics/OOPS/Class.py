import datetime

class Player:
    def __init__(self, first_name, last_name, birth_year,team):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.team = team
        self.score = []

    def add_score(self, score):
        self.score.append(score)

    def get_average(self):
        return sum(self.score)/len(self.score)

    def __lt__(self, other):
        self_avg = self.get_average()
        other_avg = other.get_average()
        return self_avg < other_avg

    def get_age(self):
        curr_year = datetime.datetime.now().year
        return curr_year - self.birth_year

virat = Player("Virat","Kohli",1988, "India")
david = Player("David","Warner",1998, "Australia")

# print(virat.first_name)
# print(virat.last_name)
# print(virat.birth_year)
virat.add_score(30)
virat.add_score(120)
virat.add_score(70)

david.add_score(34)
david.add_score(45)
david.add_score(90)

print(virat.score)
print(david.get_average())
print(virat.get_average())

print(david > virat)

print(virat.get_age())


