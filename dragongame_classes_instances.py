# Main classes
class Dragon:

    """Dragon class"""
    def __init__(self, name, element, home, heads, tails):
        self.name = name
        self.element = element
        self.home = home
        self.heads = heads
        self.tails = tails

    def cut_head(self, dmg):
        """Removes x heads from the hydra.
        If 1 was removed, grow another one.
        If 2 were removed, grow nothing back."""
        # Check to see if the hydra still has heads.
        if self.heads <= 0:
            print("\nImpossible to cut an ethereal head, try something else.")
            return False
        elif dmg >= self.heads:
            dmg = self.heads

        if dmg == 1:
            print("\nOne head was cut, but another grew in its place")
        elif dmg == 2:
            self.heads -= 2
            print("\n2 heads were cut, and nothing bad happened. What a relief!")

    def cut_tail(self, dmg):
        """Removes x tails from the hydra.
        If 1 was removed, 2 grow back.
        If 2 were removed, 1 head grows back."""
        if self.tails <= 0:
            print("\nImpossible to cut an ethereal tail, try something else.")
            return False
        elif dmg >= self.tails:
            dmg = self.tails

        if dmg == 1:
            self.tails += 1
            print("\n1 tail was cut, but 2 tails grew in its place")
        elif dmg == 2:
            self.tails -= 2
            self.heads += 1
            print("\n2 tails were cut, but it caused an extra head to grow as well")

class Player:
    """Player class"""    
    # each initial weapon is different, each bagType has different capacity
    
    def __init__(self, name, initialWeapon, home, bagType, gender):
        self.name = name
        self.weapon = initialWeapon
        self.home = home
        self.bagType = bagType
        self.gender = gender
    
    def change_weapon (self, actualWeapon, newWeapon):
            if newWeapon is not actualWeapon:
                self.weapon = newWeapon
            else:
                print ("It is not worth changing your current weapon for the same type. Try another, pall.")

    
        
# new Players
"""Player class"""
    
Weakwarrior = Player("Steve", "Short sword", "Small village", "Bag", "male")
BravePrincess = Player("Zelda", "Short sword", "Small village", "Rucksack", "male")
FashionHero = Player("Susie", "Deadly lipstick", "Hollywood", "Handbag", "female")
YoungCharlatan = Player("Lockheart", "Wand", "Big city", "Rucksack", "male")
PreyingPriest = Player("John", "Staff", "Royal capital", "Bag", "male")
BoldCoward = Player("Aussie", "Boomerang", "Scorching desert", "Rucksack", "female")
        
        
# new Dragons:
"""Dragon class"""
        
easyDragon1 = Dragon("Bob","Fire","Volcan", heads=3,tails=3)    
easyDragon2 = Dragon("Gill","Water", "Lake", heads=4,tails=4)

mediumDragon1 = Dragon("Lady","Fire","Desert", heads=5,tails=5)
mediumDragon2 = Dragon("Sechs","Lightning", "Cave", heads=6,tails=6)

hardDragon1 = Dragon("Monk","Water", "Shaolin Temple", heads=7,tails=7)
hardDragon2 = Dragon("Tomb","Earth", "Cemetery", heads=8,tails=8)
hardDragon3 = Dragon("Frosty","Ice","Glaciers",heads=8,tails=8)

secretDragon = Dragon("Chuck Norris","All elements", "Moon", heads=15,tails=15)

# dictionary with dragons and life status

#dragon_lives = {easyDragon1,"alive",easyDragon2,"alive",mediumDragon1,"alive",mediumDragon2,"alive",hardDragon1,\
#                    hardDragon2,"alive",hardDragon3,"alive",secretDragon,"alive"}

allDragons = [easyDragon1,easyDragon2,mediumDragon1,mediumDragon2,hardDragon1,hardDragon2,hardDragon3,secretDragon]                    
status = ["alive","alive","alive","alive","alive","alive","alive","alive"]
    
dragon_lives = dict(zip(allDragons, status)) # keys, values
del(status)
