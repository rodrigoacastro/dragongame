from dragongame_classes_instances import *
import random


print("Choosing your next victim...\n")
allDragons = [easyDragon1,easyDragon2,mediumDragon1,mediumDragon2,hardDragon1,hardDragon2,hardDragon3,secretDragon]
easyDragons = [easyDragon1,easyDragon2]
mediumDragons = [mediumDragon1,mediumDragon2]
hardDragons = [hardDragon1,hardDragon2,hardDragon3]
#secretDragon

newOpponent = [ allDragons[i] for i in sorted(random.sample(range(len(allDragons)), 1)) ]

print(newOpponent.name)