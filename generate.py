import action
import equipment
import enviroment
import interface
import json
import random
import dev_tools
import loot
import generate

def room(x, y):
    map_file = open("map.json", "r+")
    map_list = json.loads(map_file.read())
    room_number = str(len(map_list)+1)
    map_list[room_number] = {}
    map_list[room_number]["x"] = x
    map_list[room_number]["y"] = y
    room = enviroment.rooms()
    map_list[room_number]["size"] = room[0]
    map_list[room_number]["material"] = room[1]
    map_file.seek(0)
    map_file.truncate()
    json.dump(map_list, map_file, indent = 0)
    return room_number

def enemies(number_of_enemies, room_number):
    map_file = open("map.json", "r+")
    map_list = json.loads(map_file.read())
    map_list[room_number]["number_of_enemies"] = {}
    map_list[room_number]["number_of_enemies"] = number_of_enemies
    map_list[room_number]["enemies"] = {}
    for i in range(1, number_of_enemies+1): #Populating the room with enemies
        map_list[room_number]["enemies"][i] = random_enemy()
    map_file.seek(0)
    map_file.truncate()
    json.dump(map_list, map_file, indent = 0)
    map_file.close()

def random_enemy():
    enemies_file = open("enemies.json", "r") #Open file with list of enemies.
    enemies_list = json.loads(enemies_file.read()) #Pulling list of enemies and arranging as json.
    random_enemy = random.choice(list(enemies_list)) #Pulling a random enemy name from the list.
    enemy = enemies_list[random_enemy] #Pulling the dictonary for the enemy, by using the name generated in random_enemy line, as a key.
    return enemy

def loot(container, room_number):
    map_file = open("map.json", "r+")
    map_list = json.loads(map_file.read())
    loot_file = open("items.json", "r")
    loot_list = json.loads(loot_file.read())
    loot_type = random.choice(list(loot_list))
    random_loot = random.choice(list(loot_list[loot_type]))
    if "loot" not in map_list[room_number]:
        map_list[room_number]["loot"] = {}
        map_list[room_number]["loot"]["body"] = {}
        map_list[room_number]["loot"]["chest"] = {}
    number_of_loot_items = len(map_list[room_number]["loot"][container])
    map_list[room_number]["loot"][container][str(number_of_loot_items + 1)] = random_loot, loot_type
    print(map_list[room_number]["loot"][container])
    map_file.seek(0)
    map_file.truncate()
    json.dump(map_list, map_file, indent = 0)
    map_file.close()
