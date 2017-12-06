import action
import equipment
import enviroment
import interface
import json
import random

def change_equipment():
    equipment_file = open("equipment.txt", "r+")
    equipment_list = json.loads(equipment_file.read())
    inventory_file = open("inventory.txt", "r")
    inventory_list = json.loads(inventory_file.read())
    made_choice = False
    choose_item = input("Armour: " + equipment_list["armour"]["name"] + "\nWeapon: " + equipment_list["weapon"]["name"] + "\nWhich would you like to change? w/a/n(one)")
    while made_choice == False:
        if choose_item == "a":
            for item in inventory_list:
                if inventory_list[item]["type"] == "armour":
                    print(item + ". " + inventory_list[item]["name"])
            choose_inventory = input("What would you like to choose? (number)")
            equipment_list["armour"] = inventory_list[choose_inventory]
            equipment_file.seek(0)
            equipment_file.truncate()
            json.dump(equipment_list, equipment_file, indent = 0)
            made_choice = True
        elif choose_item == "w":
            for item in inventory_list:
                if inventory_list[item]["type"] == "weapon":
                    print(item + ". " + inventory_list[item]["name"])
            choose_inventory = input("What would you like to choose? (number)")
            equipment_list["weapon"] = inventory_list[choose_inventory]
            equipment_file.seek(0)
            equipment_file.truncate()
            json.dump(equipment_list, equipment_file, indent = 0)
            made_choice = True
        elif choose_item == "n":
            made_choice = True
        else:
            print("Please choose w/a/n")
            made_choice = False
    equipment_file.close()
