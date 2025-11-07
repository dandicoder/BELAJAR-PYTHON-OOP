class Team:
    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(self.team)

class TipeHero:
    def setTipeHero(self, hero):
        self.hero = hero

    def showHero(self):
        print(self.hero)

class Hero(Team, TipeHero):
    def __init__(self, name, health):
        self.name = name
        self.health = health


ucup = Hero("ucup", 100)


ucup.setTeam("Merah")
ucup.setTipeHero("Petarung")

ucup.showTeam()
ucup.showHero()