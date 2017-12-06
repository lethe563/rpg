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
    return health, enemies, enemy_number


def travel():

    character_file = open("character.txt", "r+")
    character = json.loads(character_file.read())
    quest = input("Which direction would you like to go? n/s/e/w")
    if quest == "n":
        character["y"] = character["y"] + 1
    elif quest == "s":
        character["y"] = character["y"] - 1
    elif quest == "e":
        character["x"] = character["x"] + 1
    elif quest == "w":
        character["x"] = character["x"] - 1

    character_file.seek(0)
    character_file.truncate()
    json.dump(character, character_file, indent = 0)

def death():
    character_file = open("character.txt", "r+")
    character = json.loads(character_file.read())

    if character["health"] <= 0:
        dead = True
        print("You are dead")
    else:
        dead = False
    return dead

def run(): #TODO calculate the chances of escaping enemy
    return False
