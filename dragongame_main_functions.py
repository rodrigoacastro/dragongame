# Dragon game Main functions

from dragongame_classes_instances import *

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
    elif dragon.heads is 1 and dragon.tails is 0:
        print("Too bad. You never the last head of the dragon devouring you after burning you whole. Try again!")
    else: # if the dragon has no heads or tails
        print("Congratulations, you have just killed the dragon! Now you can celebrate all night with your village!")
        global running
        running = False


def createNewPlayer ():
	
	# Player can create your own player interacting with the question:
	choice = input("Would you like to your own self?\n Please inform all your secrets:\n")

	if choice is "yes":
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

		NewPlayer = Player(playerName,playerWeapon,playerHome,playerBag,playerGender)
		
	elif choice is "yes":

	else:
		print("Whatever choice you would made is not important anymore, we will choose for you")
		# sample one of the ready-made heroes
		
		# https://stackoverflow.com/questions/6482889/get-random-sample-from-list-while-maintaining-ordering-of-items
		#rand_smpl = [ mylist[i] for i in sorted(random.sample(xrange(len(mylist)), 4)) ]
		
		allHeroes = [Weakwarrior,BravePrincess,FashionHero,YoungCharlatan,PreyingPriest,BoldCoward]

		#nonOriginalHero = [ allHeroes[i] for i in sorted(random.sample(xrange(len(allHeroes)), 1)) ]
		NewPlayer = [ allHeroes[i] for i in sorted(random.sample(xrange(len(allHeroes)), 1)) ]
		
	return(NewPlayer)
	
def chooseOpponent():

	print("Choosing your next victim...\n")
	allDragons = [easyDragon1,easyDragon2,mediumDragon3,mediumDragon1,mediumDragon2,hardDragon1,hardDragon2,hardDragon3,secretDragon]
	
	newOpponent = [ allDragons[i] for i in sorted(random.sample(xrange(len(allDragons)), 1)) ]
	
	return(newOpponent)
				

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