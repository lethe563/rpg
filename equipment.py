import action
import equipment
import enviroment
import interface
import json
import random
import dev_tools
import loot

def change_equipment():
    inventory_file = open("inventory.json", "r+")
    inventory_list = json.loads(inventory_file.read())
    backpack_file = open("backpack.json", "r+")
    backpack_list = json.loads(backpack_file.read())
    made_choice = False
    choose_item = input("Armour: " + inventory_list["armour"]["name"] + "\nWeapon: " + inventory_list["weapon"]["name"] + "\nWhich would you like to change? w/a/n(one)")
    while made_choice == False:
        if choose_item == "a":
            for item in backpack_list:
                if backpack_list[item]["type"] == "armour":
                    print(item + ". " + backpack_list[item]["name"])
            choose_backpack = input("What would you like to choose? (number)")
            temp_transfer = inventory_list["armour"]
            inventory_list["armour"] = backpack_list[str(choose_backpack)]
            backpack_list[str(choose_backpack)] = temp_transfer
            made_choice = True
        elif choose_item == "w":
            for item in backpack_list:
                if backpack_list[item]["type"] == "weapon":
                    print(item + ". " + backpack_list[item]["name"])
            choose_backpack = input("What would you like to choose? (number)")
            temp_transfer = inventory_list["weapon"]
            inventory_list["weapon"] = backpack_list[str(choose_backpack)]
            backpack_list[str(choose_backpack)] = temp_transfer
            made_choice = True
        elif choose_item == "n":
            made_choice = True
        else:
            print("Please choose w/a/n")
            made_choice = False
    inventory_file.seek(0)
    inventory_file.truncate()
    json.dump(inventory_list, inventory_file, indent = 0)
    backpack_file.seek(0)
    backpack_file.truncate()
    json.dump(backpack_list, backpack_file, indent = 0)
