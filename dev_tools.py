import action
import equipment
import enviroment
import interface
import json
import random
import dev_tools

def dev():
    completed = False
    while completed == False:
        tool = input("(a)dd_item (q)uit")
        if tool == "a":
            add_item()
        elif tool == "q":
            completed = True
        else:
            print("Invalid choice")

def add_item(): #Development only. Adds items to the pool of possible items in the game forever.
    item_file = open("items.json", "r+")
    item_list = json.loads(item_file.read())
    made_choice = False
    while made_choice == False:
        item_choice = input("What item would you like to add? (a)rmour (w)eapon (q)uit")
        if item_choice == "a":
            item_type = "armour"
            made_choice = True
        elif item_choice == "w":
            item_type = "weapon"
            made_choice = True
        elif item_choice == "q":
            break
        else:
            print("invalid selection")
    if made_choice == True: #Only way this doesn't happen is if the developer chose "q"
        name = input("Name: ")
        rating = input("Rating (attack or defence): ")
        description = input("description: ")
        item_list[item_type][name] = {}
        item_list[item_type][name]["rating"] = rating
        item_list[item_type][name]["description"] = description
        item_file.seek(0)
        item_file.truncate()
        json.dump(item_list, item_file, indent = 0)
