import action
import equipment
import enviroment
import interface
import json
import random
import dev_tools
import loot
import generate

default_player_health = 100
default_player_attack = 10
default_player_x_location = 0
default_player_y_location = 0

def generator():
    map_file = open("map.json", "r+")
    map_list = json.loads(map_file.read())
    character_file = open("character.json", "r")
    character = json.loads(character_file.read())
    current_x = character["x"]
    current_y = character["y"]
    traveled_to = False
    for room in map_list:
        if map_list[room]["x"] == current_x and map_list[room]["y"] == current_y:
            print("Room alrady traveled to.")
            traveled_to = True
            break

    if traveled_to == False:
        room_number = generate.room(current_x, current_y)
        number_of_enemies = random.randrange(1, 4)
        generate.enemies(number_of_enemies, room_number)
        number_of_chests = random.randrange(1, 4)
        print(number_of_chests)
        for i in range(number_of_chests):
            generate.loot("chest", room_number)


def rooms():
    material_list = ["Wood", "Stone", "Metal", "Mud"] #Possible materials
    material = random.choice(material_list) #Choosing the material at random
    size_list = ["Small", "Medium", "Big"] #Possible sizes of the rooms
    size = random.choice(size_list) #Choosing the size of the room at random
    room = [size, material] #Building room
    return room

def current_room(current_x, current_y):
    map_file = open("map.json", "r+")
    map_list = json.loads(map_file.read())
    enemies = {}
    room_number = ""
    size = ""
    material = ""
    number_of_enemies = ""
    for i in map_list:
        if map_list[i]["x"] == current_x and map_list[i]["y"] == current_y:
            room_number = i
            size = map_list[i]["size"]
            material = map_list[i]["material"]
            size = map_list[str(i)]["size"]
            material = map_list[str(i)]["material"]
            number_of_enemies = int(map_list[str(i)]["number_of_enemies"])
            for j in range(1, number_of_enemies + 1):
                enemies[j] = {}
                enemies[j]["name"] = map_list[str(i)]["enemies"][str(j)]["name"]
                enemies[j]["health"] = float(map_list[i]["enemies"][str(j)]["health"])
                enemies[j]["attack"] = int(map_list[i]["enemies"][str(j)]["attack"])
    return room_number, size, material, enemies, number_of_enemies

def change_current_room(room_number, enemy_health, enemy_number):
    map_file = open("map.json", "r+")
    map_list = json.loads(map_file.read())
    total_enemies = map_list[room_number]["number_of_enemies"]
    if enemy_health <= 0:
        for i in range(len(map_list[str(room_number)]["enemies"][str(enemy_number)])): #reason for the range() and len() is because otherwise the for loop itterates randomly
            if int(i) >= int(enemy_number) and int(i) < total_enemies:
                map_list[room_number]["enemies"][str(i)] = map_list[room_number]["enemies"][str(i+1)]
        del map_list[str(room_number)]["enemies"][str(total_enemies)]
        generate.loot("body", room_number)
        map_list[str(room_number)]["number_of_enemies"] -= 1
    else:
        map_list[room_number]["enemies"][str(enemy_number)]["health"] = enemy_health
    map_file.seek(0)
    map_file.truncate()
    json.dump(map_list, map_file, indent = 0)

def generate_character():
    character_file = open("character.json", "w")
    character = {}
    character["health"] = default_player_health
    character["attack"] = default_player_attack
    character["x"] = default_player_x_location
    character["y"] = default_player_y_location
    character_file.seek(0)
    character_file.truncate()
    json.dump(character, character_file, indent = 0)

def change_character(health, x, y): #If location unchanged, pass in 0, 0 for x, y
        character_file = open("character.json", "r+")
        character = json.loads(character_file.read())
        character["health"] = health
        character["attack"] = 10
        if x == 0 and y == 0: #Doesn't effect if the character is at 0, 0
            character["x"] = character["x"]
            character["y"] = character["y"]
        else:
            character["x"] = x
            character["y"] = y
        character_file.seek(0)
        character_file.truncate()
        json.dump(character, character_file, indent = 0)
