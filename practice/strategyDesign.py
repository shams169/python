"""
class Fighter:

    def __init__(self, name=None, health=100):
        self.name = name
        self.health = health

    def attack(self, opponent):
        print(f'{self.name} attacked {opponent.name}')
    
    def defend(self, attacker):
        print(f'{self.name} defended from {attacker.name}')


player1 = Fighter(name="Rocky")
player2 = Fighter(name="Apollo")

player1.attack(player2)
player2.attack(player2)
player1.defend(player2)
player2.defend(player2)
"""

# Create subclasses of fighter that differentiate fighter from each other based on the looks.
# But there is one problem since this is a mix martial art game a fighter could choose from any of the 
# fighting styles (Muay Thai, Karate, Kungfu, Jiu-Jutsu)

"""
So the solution here is to create two base classes 
1. Fighter 
2. Styles 

Now we can have subclasses for each fighter type and subclasses for each Style type and
we can decide on the run time what type of style the fighter would like to pick

"""

class Fighter:

    def __init__(self, name=None, health=100):
        self.name = name
        self.health = health
        self.fighting_style = Style()
    
    def attack(self, attacker, opponent):
        self.fighting_style.attack(attacker, opponent)
        
    def defend(self, attacker, opponent):
        self.fighting_style.defend(attacker, opponent)


class Asian(Fighter):

    def __init__(self, name=None, health=100, fighting_style=None):
        super(Asian, self).__init__(name, health)
        self.fighting_style = fighting_style

    def looks(self):
        print(f'{self.name} has Asian looks')



#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#

class Style:

    def attack(self, opponent):
        pass

    def defend(self, attacker):
        pass
    

class MuayThai(Style):
    def __init__(self):
        super(MuayThai, self).__init__()

    def attack(self, attacker, opponent):
        message = f'{attacker.name} is attacking {opponent.name} in Muay Thai style '
        print(message)

    def defend(self, attacker, opponent):
        message = f'{opponent.name} is defending {opponent.name} in Muay Thai style '
        print(message)


class KungFu(Style):
    def __init__(self):
        super(KungFu, self).__init__()

    def attack(self, attacker, opponent):
        message = f'{attacker.name} is attacking {opponent.name} in KungFu style '
        print(message)

    def defend(self, attacker, opponent):
        message = f'{opponent.name} is defending {opponent.name} in KungFu style '
        print(message)

class JuiJutsu(Style):
    def __init__(self):
        super(JuiJutsu, self).__init__()

    def attack(self, attacker, opponent):
        message = f'{attacker.name} is attacking {opponent.name} in JuiJutsu style '
        print(message)

    def defend(self, attacker, opponent):
        message = f'{opponent.name} is defending {opponent.name} in JuiJutsu style '
        print(message)


f1 = Asian(name='Rocky', health=100, fighting_style=MuayThai())
f2 = Asian(name='Apollo', health=100, fighting_style=JuiJutsu())


f1.attack(f1, f2)
f2.attack(f2, f1)