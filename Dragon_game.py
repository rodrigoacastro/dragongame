# Main classes
class Dragon:
    """Dragon class."""
    def __init__(self, heads, tails):
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
            dmg == self.heads

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
            dmg == self.tails

        if dmg == 1:
            self.tails += 1
            print("\n1 tail was cut, but 2 tails grew in its place")
        elif dmg == 2:
            self.tails -= 2
            self.heads += 1
            print("\n2 tails were cut, but it caused an extra head to grow as well")


# Main functions
def show_rules():
    """Show the rules to the player"""
    file = open("Rules.txt","r")
    for item in file:
        print(item)

def show_combatRules():
    """Show the rules to the player"""
    file = open("CombatRules.txt","r")
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
    global running
    """Check if number of heads is 1 (if so, it is game over)"""
    if dragon.heads == 1 and dragon.tails == 0:
        print("Too bad. You never saw the last head of the dragon devouring you after burning you whole. Try again!")
        running = False
    elif dragon.heads == 0 and dragon.tails == 0: # if the dragon has no heads or tails
        print("Congratulations, you have just killed the dragon! Now you can celebrate all night with your village!")
        running = False
    else:
        print("Lucky, you are STILL alive, but not for long...")



def player_action(choice, dragon):

    show_combatRules()
    #print ("type quit to leave game")
    
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
    #elif choice == 'quit':
     #   return ("Thanks for playing! =)")
    else:
        print("Invalid option. Try again.")


# Initialization
running = True

drag = Dragon(heads=3,tails=3)

print("Welcome to Dragongame")
check_dragon(drag)
print("Your objective is to kill the evil dragon, before he kills you and your whole village, Riverville\n")

show_rules()

print("To (try to) kill the evil dragon you can: \n1) cut 1 head; \n2) cut 2 heads; \n3) cut 1 tail; \n4) cut 2 tails.")
print("\nWhat will you do?")

# Main loop
while running:
    action = input("Type 1 to 4 to select an option: ")
    player_action(action, drag)
