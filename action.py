import action
import equipment
import enviroment
import interface
import json
import random

def combat(health, attack, enemies, enemy_number, room_number):
    print("attack: " + str(attack))
    enemies[enemy_number]["health"] -= attack * random.random() #Damage inflicted on enemy is your attack rating times a random number between 0 and 1
    health -= enemies[enemy_number]["attack"] * random.random() #Damage inflicted on you is your enemy's attack rating times a random number between 0 and 1
    if enemies[enemy_number]["health"] <= 0:
        print("Your enemy is defeated!")
    enviroment.change_current_room(room_number, enemies[enemy_number]["health"], enemy_number, health)

def next_step(first_time, current_x, current_y):
    decision = False #Decision to continue on quest
    continue_quest = True
    while decision == False: #Continue loop until a decision is reached
        if first_time == True:
            quest = input("Would you like to start your quest? y/n/equip") #e is for equip testing
        else:
            quest = input("What would you like to do? /n/s/e/w/equip/q")

        if quest == "y":
            decision = True
        elif quest == "n":
            decision = True
            current_y = current_y + 1
        elif quest == "s":
            decision = True
            current_y = current_y - 1
        elif quest == "e":
            decision = True
            current_x = current_x + 1
        elif quest == "w":
            decision = True
            current_y = current_y - 1
        elif quest == "q": #End game
            decision = True #To break the while decision loop
            continue_quest = False
            print("Goodbye!")
        elif quest == "equip":
            equipment.change_equipment()
        else:
            print("Please enter either y or n.")
            decision = False #Go through the while decision loop again

    return current_x, current_y, continue_quest

def death(health):
    dead = True
    if health <= 0:
        dead = True
        print("You are dead")
    else:
        dead = False
    return dead

def run(): #TODO calculate the chances of escaping enemy
    return False
