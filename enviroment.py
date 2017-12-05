import action
import equipment
import enviroment
import json
import random

def generator(input_x, input_y):
    map_file = open("map.txt", "r+")
    map_list = json.loads(map_file.read())
    traveled_to = False
    for room in map_list:
        if map_list[room]["x"] == input_x and map_list[room]["y"] == input_y:
            print("Room alrady traveled to.")
            traveled_to = True
            break

    if traveled_to == False:
        new_length_of_list = len(map_list)+1
        map_list[new_length_of_list] = {}
        map_list[new_length_of_list]["x"] = input_x
        map_list[new_length_of_list]["y"] = input_y
        room = rooms()
        map_list[new_length_of_list]["size"] = room[0]
        map_list[new_length_of_list]["material"] = room[1]
        number_of_baddies = range(1, 4)
        map_list[new_length_of_list]["baddies"] = {}
        for i in number_of_baddies: #Populating the room with enemies
            map_list[new_length_of_list]["number_of_baddies"] = str(i)
            map_list[new_length_of_list]["baddies"][i] = baddies()
        map_file.seek(0)
        map_file.truncate()
        json.dump(map_list, map_file, indent = 0)

def rooms():
    material_list = ["Wood", "Stone", "Metal", "Mud"] #Possible materials
    material = random.choice(material_list) #Choosing the material at random
    size_list = ["Small", "Medium", "Big"] #Possible sizes of the rooms
    size = random.choice(size_list) #Choosing the size of the room at random
    room = [size, material] #Building room
    return room

def baddies():
    baddies_file = open("baddies.txt", "r") #Open file with list of enemies.
    baddies_list = json.loads(baddies_file.read()) #Pulling list of enemies and arranging as json.
    random_baddie = random.choice(list(baddies_list)) #Pulling a random enemy name from the list.
    baddie = baddies_list[random_baddie] #Pulling the dictonary for the enemy, by using the name generated in random_baddie line, as a key.
    return baddie

def current_room(current_x, current_y):
    map_file = open("map.txt", "r+")
    map_list = json.loads(map_file.read())
    baddies = {}
    for i in map_list:
        if map_list[i]["x"] == current_x and map_list[i]["y"] == current_y:
            room_number = i
            size = map_list[i]["size"]
            material = map_list[i]["material"]
            for j in map_list[str(room_number)]["baddies"]:
                #baddies["number"] = str(j)
                baddies[j] = {}
                baddies[str(j)]["name"] = map_list[str(room_number)]["baddies"][str(j)]["name"]
                baddies[str(j)]["health"] = float(map_list[i]["baddies"][str(j)]["health"])
                baddies[str(j)]["attack"] = int(map_list[i]["baddies"][str(j)]["attack"])
                #baddies[str(j)]["room_number"] = i
            #baddie_name = map_list[i]["baddies"]["name"]
            #baddie_health = float(map_list[i]["baddies"]["health"])
            #baddie_attack = float(map_list[i]["baddies"]["attack"])
    return room_number, size, material, baddies

def change_current_room(room_number, enemy_health, baddie_number):
        map_file = open("map.txt", "r+")
        map_list = json.loads(map_file.read())
        if enemy_health <= 0:
            del map_list[str(room_number)]["baddies"]["1"]
        else:
            map_list[room_number]["baddies"]["1"]["health"] = enemy_health
        map_file.seek(0)
        map_file.truncate()
        json.dump(map_list, map_file, indent = 0)
