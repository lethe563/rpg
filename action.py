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
    enviroment.change_current_room(room_number, enemies[enemy_number]["health"], enemy_number)
    enviroment.change_character(health, 0, 0)


def travel(current_x, current_y):

    if quest == "n":
        current_y = current_y + 1
    elif quest == "s":
        current_y = current_y - 1
    elif quest == "e":
        current_x = current_x + 1
    elif quest == "w":
        current_y = current_y - 1


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
