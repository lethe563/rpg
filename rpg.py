import action
import equipment
import enviroment
import interface
import json
import random
import dev_tools

def main():
    current_x = 0
    current_y = 0
    enviroment.generate_character()
    first_time = True
    continue_quest = True
    dead = False #If the user is dead, change to True
    while dead == False: #While the player is still alive

        if first_time == True:
            continue_quest = interface.initial()
            first_time = False
        if continue_quest == False:
            print("Goodbye")
            break
        enviroment.generator()
        continue_quest = interface.room()
        dead = action.death()



main()
