import action
import equipment
import enviroment
import interface
import json
import random
import dev_tools
import loot

def create_loot(container, room_number):
    map_file = open("map.json", "r+")
    map_list = json.loads(map_file.read())
    loot_file = open("items.json", "r")
    loot_list = json.loads(loot_file.read())
    loot_type = random.choice(list(loot_list))
    random_loot = random.choice(list(loot_list[loot_type]))
    number_of_loot_items = len(map_list[room_number]["loot"][container])
    map_list[room_number]["loot"][container][number_of_loot_items + 1] = random_loot, loot_type
    print(map_list[room_number]["loot"][container])
    map_file.seek(0)
    map_file.truncate()
    json.dump(map_list, map_file, indent = 0)

def take_loot(room_number):
    map_file = open("map.json", "r+")
    map_list = json.loads(map_file.read())
    items_file = open("items.json", "r")
    items_list = json.loads(items_file.read())
    backpack_file = open("backpack.json", "r+")
    backpack_list = json.loads(backpack_file.read())
    choose_item = False
    loot_choice = False
    made_choice = False
    while made_choice == False:
        loot_choice = input("would you like to take loot from a (b)ody or a (c)hest?") #I believe this approach will make more sense for a gui in the finished product.
        if loot_choice == "b":
            loot_container = "body"
            made_choice = True
        elif loot_choice == "c":
            loot_container = "chest"
            made_choice = True
        else:
            print("Please choose either (b)ody or (c)hest")

#    number_of_items = len(map_list[room_number]["loot"][loot_container])
    for item in (map_list[room_number]["loot"][loot_container]):
        print(str(item) + ": " + str(map_list[room_number]["loot"][loot_container][item][0]) + " (" + str(map_list[room_number]["loot"][loot_container][item][1]) + ")")
    loot_choice = input("What would you like to take (number) (0 for quit)?: ")
    if loot_choice != "0":
        loot_item = map_list[room_number]["loot"][loot_container][loot_choice][0]
        loot_type = map_list[room_number]["loot"][loot_container][loot_choice][1]
        for i in range(len(map_list[room_number]["loot"][loot_container])): #reason for the range() and len() is because otherwise the for loop itterates randomly
            print(i)
            if i >= int(loot_choice) and int(i) < len(map_list[room_number]["loot"][loot_container]):
                map_list[room_number]["loot"][loot_container][str(i)] = map_list[room_number]["loot"][loot_container][str(int(i)+1)]
        del map_list[room_number]["loot"][loot_container][str(len(map_list[room_number]["loot"][loot_container]))]
        print(loot_item)
        backpack_list[str(len(backpack_list)+1)] = {}
        backpack_list[str(len(backpack_list))]["name"] = loot_item
        backpack_list[str(len(backpack_list))]["type"] = loot_type
        backpack_list[str(len(backpack_list))]["rating"] = items_list[loot_type][loot_item]["rating"]
        backpack_list[str(len(backpack_list))]["description"] = items_list[loot_type][loot_item]["description"]


    backpack_file.seek(0)
    backpack_file.truncate()
    json.dump(backpack_list, backpack_file, indent = 0)
    map_file.seek(0)
    map_file.truncate()
    json.dump(map_list, map_file, indent = 0)
