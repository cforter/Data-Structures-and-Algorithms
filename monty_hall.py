#
# Monty Hall game simulation
#

import random

def goat_game(guess, answer):

    doors = ["goat","goat","car"]
    random.shuffle(doors)
    index = [0,1,2]
    
    guess = int(guess) - 1 # because list index starts at 0
    chosen_door = doors[guess]
    index.pop(guess)

    if chosen_door == "car":
        door_open = random.randint(0, (len(index) - 1))
        index.pop(door_open)
        
    else:
        if doors[index[0]] == "goat":
            index.pop(0)
        else:
            index.pop(1)
            
    if answer == "n":
        final_answer = chosen_door
        
    if answer == "y":
        final_answer = doors[index[0]] # we removed guess and the opened door so all that's left is the third door
        
    if final_answer == "goat":
        return "goat"
    else:
        return "car"

# main
switch = [goat_game(2,"y") for _ in range(10000)]
print(switch.count("goat"))

no_switch = [goat_game(2,"n") for _ in range(10000)]
print(no_switch.count("goat"))   
