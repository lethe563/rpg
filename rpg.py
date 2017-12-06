import action
import equipment
import enviroment
import interface
import json
import random

def main():
    current_x = 0
    current_y = 0
    health = 100.0 #User's health
    attack = 10 #User's attack strength
    first_time = True
    continue_quest = True
    dead = False #If the user is dead, change to True
    while dead == False: #While the player is still alive
        enviroment.generate_character()
        if first_time == True:
            continue_quest = interface.initial()
            first_time = False
        if continue_quest == False:
            print("Goodbye")
            break
        enviroment.generator(current_x, current_y)
        interface.room()
        dead = action.death(health)



main()
