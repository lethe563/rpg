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

        for i in range(1, 3): #Populating the room with enemies
            map_list[new_length_of_list]["baddie" + str(i)]=baddies()
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
    for i in map_list:
        if map_list[i]["x"] == current_x and map_list[i]["y"] == current_y:
            room_number = i
            size = map_list[i]["size"]
            material = map_list[i]["material"]
            baddie_name = map_list[i]["baddie1"]["name"]
            baddie_health = float(map_list[i]["baddie1"]["health"])
            baddie_attack = float(map_list[i]["baddie1"]["attack"])
    return room_number, size, material, baddie_name, baddie_health, baddie_attack
