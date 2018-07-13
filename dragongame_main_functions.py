# Dragon game Main functions

from dragongame_classes_instances import *
import random

def show_rules():
    """Show the rules to the player"""
    file = open("Rules.txt","r")
    for item in file:
        print(item)


def mostrar_regras():
    """Show the rules to the player in Portuguese"""
    file = open("Regras.txt","r")
    for item in file:
        print(item)


def check_dragon(dragon):
    """Check data on the dragon (number of heads and tails)"""
    print("\nThe dragon has %i heads." %dragon.heads)
    print("The dragon has %i tails.\n" %dragon.tails)


def check_game_over(dragon):
    """Check if number of heads is 1 (if so, it is game over)"""
    if dragon.heads > 1 or dragon.tails >= 1:
        print("Lucky, you are STILL alive, but not for long...")
    elif dragon.heads == 1 and dragon.tails == 0:
        print("Too bad. You never the last head of the dragon devouring you after burning you whole. Try again!")
    else: # if the dragon has no heads or tails
        print("Congratulations, you have just killed the dragon! Now you can celebrate all night with your village!")
        global running
        running = False

def createNewPlayer ():
    
    # Player can create your own player interacting with the question:
    choice = input("Would you like to your own self? yes or no?")

# CHANGE: give choices for weapon, recipient and Gender and select from them
    if choice == "yes":
        print("Please inform all your secrets:\n")
        # Which name will take you to Glory (or to the Heavens)?
        playerName = input("Which name will take you to Glory (or to the Heavens)?")
        # Which weapon will hurt others (but mainly you)?
        playerWeapon = input("Which weapon will hurt others (but mainly you)?")
        # Which place have you been born into?
        playerHome = input("Which place have you been born into?")
        # Which recipient allows you carry so much junk, ops, luggage?
        playerBag = input("Which recipient allows you carry so much junk, ops, luggage?")
        # Are you a future lord or future lady?
        playerGender = input("Are you a future lord or future lady?")

        newPlayer = Player(playerName,playerWeapon,playerHome,playerBag,playerGender)

        return (newPlayer)

    elif choice == "no":

        print("Whatever choice you would make is not important anymore, we will choose for you")
        # sample one of the ready-made heroes
        
        # https://stackoverflow.com/questions/6482889/get-random-sample-from-list-while-maintaining-ordering-of-items
        #rand_smpl = [ mylist[i] for i in sorted(random.sample(xrange(len(mylist)), 4)) ]
        
        allHeroes = [Weakwarrior,BravePrincess,FashionHero,YoungCharlatan,PreyingPriest,BoldCoward]

        #nonOriginalHero = [ allHeroes[i] for i in sorted(random.sample(xrange(len(allHeroes)), 1)) ]
        newPlayer = [ allHeroes[i] for i in sorted(random.sample(range(len(allHeroes)), 1)) ]

        return(newPlayer)

    def printPlayerInfo(newPlayer):

        print("Your personal info:")
        print("Your name is %s." % newPlayer[0].name)
        print("Your initial weapon is %s." % newPlayer[0].weapon)
        print("Your home is %s." % newPlayer[0].home)
        print("You carry your stuff in a %s." % newPlayer[0].bagType)
        print("You are %s." % newPlayer[0].gender)
    
#def chooseOpponent():
#
#    print("Choosing your next victim...\n")
#    allDragons = [easyDragon1,easyDragon2,mediumDragon3,mediumDragon1,mediumDragon2,hardDragon1,hardDragon2,hardDragon3,secretDragon]
#    
#    newOpponent = [ allDragons[i] for i in sorted(random.sample(xrange(len(allDragons)), 1)) ]
#    
#    return(newOpponent)

# HELP WANTED
def chooseOpponent(oldOpponent=None,status="alive"):
    
    #allDragons = [easyDragon1,easyDragon2,mediumDragon1,mediumDragon2,hardDragon1,hardDragon2,hardDragon3,secretDragon]
    #status = ["alive","alive","alive","alive","alive","alive","alive","alive"]

    #dragon_lives = {easyDragon1,"alive",easyDragon2,"alive",mediumDragon1,"alive",
    #                mediumDragon2,"alive",hardDragon1,hardDragon2,"alive",
    #                hardDragon3,"alive",secretDragon,"alive"}

    allDragons = [easyDragon1, easyDragon2, mediumDragon1, mediumDragon2,
                  hardDragon1, hardDragon2, hardDragon3, secretDragon]

    allDragonNames = [easyDragon1.name,easyDragon2.name,mediumDragon1.name,mediumDragon2.name,
                    hardDragon1.name,hardDragon2.name,hardDragon3.name,secretDragon.name]
    
    dragon_status=["alive","alive","alive","alive","alive","alive","alive","alive"]
    dragon_status2=["dead","alive","alive","alive","alive","alive","alive","alive"]

    
    dragon_lives = dict(zip(allDragonNames, dragon_status)) # keys, values
    dragon_lives2 = dict(zip(allDragonNames, dragon_status2)) # keys, values

    # print dict of dragon names and lives
    for key, value in dragon_lives.items() :
        print (key, value)

    # choosing new opponent

    drag_range = range(1,len(dragon_lives.values() ))
    #for drag in dragon_lives:
    for drag,inds in dragon_lives.keys(), drag_range:
        if dragon_lives[drag] == "alive":
            newOpponent = allDragons[inds]
        elif dragon_lives[drag] == "dead":
            if drag == len(dragon_lives.values())-1: # if it is the last dragon
                print("Congratulations, you have killed all the dragons! Take your prize asap or it will disappear!")
            else:
                pass
        
    
    print("Choosing your next victim...\n")
    allDragons = [easyDragon1,easyDragon2,mediumDragon1,mediumDragon2,hardDragon1,hardDragon2,hardDragon3,secretDragon]
    easyDragons = [easyDragon1,easyDragon2]
    mediumDragons = [mediumDragon1,mediumDragon2]
    hardDragons = [hardDragon1,hardDragon2,hardDragon3]
    #secretDragon

    #newOpponent = [ allDragons[i] for i in sorted(random.sample(xrange(len(allDragons)), 1)) ]
    
    return(newOpponent)
    
    
    
"""
# new Players
""""Player class""""
    
Weakwarrior = Player("Steve", "Short sword", "Small village", "Bag", "male")
BravePrincess = Player("Zelda", "Short sword", "Small village", "Rucksack", "male")
FashionHero = Player("Susie", "Deadly lipstick", "Hollywood", "Handbag", "female")
YoungCharlatan = Player("Lockheart", "Wand", "Big city", "Rucksack", "male")
PreyingPriest = Player("John", "Staff", "Royal capital", "Bag", "male")
BoldCoward =  Player("Aussie", "Boomerang", "Scorching desert", "Rucksack", "female")
        
        
# new Dragons:
    """"Dragon class""""
        
easyDragon1 = Dragon("Bob","Fire","Volcan", heads=3,tails=3)    
easyDragon2 = Dragon("Gill","Water", "Lake", heads=4,tails=4)

mediumDragon1 = Dragon("Lady","Fire","Desert", heads=5,tails=5)
mediumDragon2 = Dragon("Sechs","Lightning", "Cave", heads=6,tails=6)

hardDragon1 = Dragon("Monk","Water", "Shaolin Temple", heads=7,tails=7)
hardDragon2 = Dragon("Tomb","Earth", "Cemetery", "heads=8,tails=8)
hardDragon3 = Dragon("Frosty","Ice","Glaciers",heads=8,tails=8)

secretDragon = Dragon("Chuck Norris","All elements", "Moon", heads=10,tails=15)
"""


def player_action(choice, dragon):
    if choice == '1':
        dragon.cut_head(1)
        check_dragon(dragon)
        check_game_over(dragon)
    elif choice == '2':
        dragon.cut_head(2)
        check_dragon(dragon)
        check_game_over(dragon)
    elif choice == '3':
        dragon.cut_tail(1)
        check_dragon(dragon)
        check_game_over(dragon)
    elif choice == '4':
        dragon.cut_tail(2)
        check_dragon(dragon)
        check_game_over(dragon)
    else:
        print("Invalid option. Try again.")