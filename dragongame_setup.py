# Dragongame

#from dragongame_classes_instances import *
from dragongame_main_functions import *


# Main classes

# dragongame_classes_instances


# Main functions

# dragongame_main_functions

# IMPLEMENTATIONS - MODIFY code below to use the following functions

# createNewPlayer()
# chooseOpponent()
# 

# Initialization
running = True



print("Welcome to Dragongame")
print("Your objective is to kill the evil dragon, before he kills you and your whole village, Riverville\n")

show_rules()

print("To (try to) kill the evil dragon you can: \n1) cut 1 head; \n2) cut 2 heads; \n3) cut 1 tail; \n4) cut 2 tails.")
print("\nWhat will you do?")

newPlayer = createNewPlayer()
opponent = chooseOpponent()

check_dragon(opponent)

# Main loop
while running:
    action = input("Type 1 to 4 to select an option: ")
    player_action(action, opponent)