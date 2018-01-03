import action
import equipment
import enviroment
import interface
import json
import random
import dev_tools
import loot

def initial():
    quest = input("Would you like to begin? y/n ")
    if quest == "y":
        start = True
    elif quest == "n":
        start = False
    else:
        print("Please answer 'y' or 'n'")
    return start

def room():
    character_file = open("character.json", "r")
    character_list = json.loads(character_file.read())
    current_x = character_list["x"]
    current_y = character_list["y"]
    health = character_list["health"]
    attack = character_list["attack"]
    continue_quest = True
    room_number, room_size, room_material, enemies, number_of_enemies = enviroment.current_room(current_x, current_y)
    print_current_room(current_x, current_y)
    decision = input("What would you like to do? (a)ttack, (t)ravel, (e)quipment, (q)uit (d)ev (l)oot: ") #(d)ev is for development only. Will be removed in the full game.
    if decision == "a":
        attack_mode = True
        while attack_mode == True:
            attack_enemy_number = int(input("Which enemy would you like to attack? 0 for run"))
            if attack_enemy_number == 0:
                attack_mode = action.run()
            elif attack_enemy_number <= number_of_enemies:
                health, enemies, number_of_enemies = action.combat(health, attack, enemies, attack_enemy_number, room_number)
                print_current_room(current_x, current_y)
    elif decision == "t":
        action.travel()
    elif decision == "e":
        equipment.change_equipment()
    elif decision == "q":
        continue_quest = False
    elif decision == "d":
        dev_tools.dev(room_number)
    elif decision == "l":
        loot.take_loot(room_number)

    return continue_quest

def print_current_room(current_x, current_y):
    room_number, room_size, room_material, enemies, number_of_enemies = enviroment.current_room(current_x, current_y)
    for i in enemies:
        print(str(i) + str(enemies[i]["name"]) + str(enemies[i]["health"]) + " " + str(enemies[i]["attack"]))
