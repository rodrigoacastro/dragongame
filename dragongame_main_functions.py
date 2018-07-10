# Dragon game

# Main functions
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