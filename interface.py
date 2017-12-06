import action
import equipment
import enviroment
import interface
import json
import random

def initial():
    quest = input("Would you like to begin? y/n ")
    if quest == "y":
        start = True
    elif quest == "n":
        start = False
    else:
        print("Please answer 'y' or 'n'")
    return start

def room(current_x, current_y, health, attack):
    room_number, room_size, room_material, enemies, number_of_enemies = print_current_room(current_x, current_y)

    decision = input("What would you like to do? (a)ttack, ")
    if decision == "a":
        attack_mode = True
        while attack_mode == True:
            attack_enemy_number = int(input("Which enemy would you like to attack? 0 for run"))
            if attack_enemy_number == 0:
                attack_mode = action.run()
            elif attack_enemy_number <= number_of_enemies:
                health = action.combat(health, attack, enemies, attack_enemy_number, room_number)
                room_number, room_size, room_material, enemies, number_of_enemies = print_current_room(current_x, current_y)


def print_current_room(current_x, current_y):
    room_number, room_size, room_material, enemies, number_of_enemies = enviroment.current_room(current_x, current_y)
    for i in enemies:
        print(str(i) + str(enemies[i]["name"]) + str(enemies[i]["health"]) + " " + str(enemies[i]["attack"]))
    return room_number, room_size, room_material, enemies, number_of_enemies
