import action
import equipment
import enviroment
import interface
import json
import random
import dev_tools

def change_equipment():
    inventory_file = open("inventory.json", "r+")
    inventory_list = json.loads(inventory_file.read())
    backpack_file = open("backpack.json", "r")
    backpack_list = json.loads(backpack_file.read())
    made_choice = False
    choose_item = input("Armour: " + inventory_list["armour"]["name"] + "\nWeapon: " + inventory_list["weapon"]["name"] + "\nWhich would you like to change? w/a/n(one)")
    while made_choice == False:
        if choose_item == "a":
            for item in backpack_list:
                if backpack_list[item]["type"] == "armour":
                    print(item + ". " + backpack_list[item]["name"])
            choose_backpack = input("What would you like to choose? (number)")
            inventory_list["armour"] = backpack_list[choose_backpack]
            inventory_file.seek(0)
            inventory_file.truncate()
            json.dump(inventory_list, inventory_file, indent = 0)
            made_choice = True
        elif choose_item == "w":
            for item in backpack_list:
                if backpack_list[item]["type"] == "weapon":
                    print(item + ". " + backpack_list[item]["name"])
            choose_backpack = input("What would you like to choose? (number)")
            inventory_list["weapon"] = backpack_list[choose_backpack]
            inventory_file.seek(0)
            inventory_file.truncate()
            json.dump(inventory_list, inventory_file, indent = 0)
            made_choice = True
        elif choose_item == "n":
            made_choice = True
        else:
            print("Please choose w/a/n")
            made_choice = False
    inventory_file.close()

def loot(container, room_number):
    map_file = open("map.json", "r+")
    map_list = json.loads(map_file.read())
    loot_file = open("items.json", "r")
    loot_list = json.loads(loot_file.read())
    loot_type = random.choice(list(loot_list))
    random_loot = random.choice(list(loot_list[loot_type]))
    print(random_loot)

    map_list[room_number][container] = random_loot
    map_file.seek(0)
    map_file.truncate()
    json.dump(map_list, map_file, indent = 0)
