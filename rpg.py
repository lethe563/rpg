import json
import random

def combat(health, attack, enemy_name, enemy_health, enemy_attack):
    #print("Enemy name: " + enemy_name + "\nEnemy health: " + str(enemy_health) + "\nCurrent health : " + str(health))
    while health > 0 and enemy_health > 0:
        command = input("Do you wish to attack? (y/n)d")
        if command == "y":
            enemy_health -= attack * random.random() #Damage inflicted on enemy is your attack rating times a random number between 0 and 1
            health -= enemy_attack * random.random() #Damage inflicted on you is your enemy's attack rating times a random number between 0 and 1
            print("Success!\nYour health is now: " + str(health) + "\nYour enemy's health is now: " + str(enemy_health))
        elif command == "n":
            health -= enemy_attack
            print("Failure! Just press y next time!\nYour health is now: " + str(health) + "\nYour enemy's health is now: " + str(enemy_health))
        elif command == "d": #Die for testing
            break
        else:
            print("Please enter either y or n.")

    return(health)

def equipment():
    equipment_file = open("equipment.txt", "r+")
    equipment_list = json.loads(equipment_file.read())
    inventory_file = open("inventory.txt", "r")
    inventory_list = json.loads(inventory_file.read())
    made_choice = False
    choose_item = input("Armour: " + equipment_list["armour"]["name"] + "\nWeapon: " + equipment_list["weapon"]["name"] + "\nWhich would you like to change? w/a/n(one)")
    while made_choice == False:
        if choose_item == "w":
            for item in inventory_list:
                if inventory_list[item]["type"] == "weapon":
                    print(item + ". " + inventory_list[item]["name"])
            choose_inventory = input("What would you like to choose? (number)")
            equipment_list["weapon"] = inventory_list[choose_inventory]
            equipment_file.seek(0)
            equipment_file.truncate()
            #equipment_file = equipment_list
            json.dump(equipment_list, equipment_file, indent = 0)
            made_choice = True

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



        elif choose_item == "n":
            made_choice = True

        else:
            print("Please choose w/a/n")
            made_choice = False

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

def next_step(first_time):
    decision = False #Decision to continue on quest
    while decision == False: #Continue loop until a decision is reached
        if first_time == True:
            quest = input("Would you like to start your quest? y/n/i/e/we") #i is for inventory testing. e is for equip testing
        else:
            quest = input("Would you like to continue your quest? y/n/i/e/we") #i is for inventory testing

        if quest == "y": #Continue game
            decision = True #Break the while decision loop
            room = rooms()
            baddie = baddies()
        elif quest == "n": #End game
            decision = True #To break the while decision loop
            room = "quit"
            baddie = "quit"
            print("Goodbye!")
        elif quest == "i":
            retrieve_inventory()
        elif quest == "e":
            equipment()
        elif quest == "we":
            write_eqipment()
        else:
            print("Please enter either y or n.")
            decision = False #Go through the while decision loop again

    return room, baddie

def death(health):
    dead = True
    if health <= 0:
        dead = True
        print("You are dead")
    else:
        dead = False
    return dead

def main():
    health = 100 #User's health
    attack = 10 #User's attack strength
    first_time = True
    dead = False #If the user is dead, change to True
    while dead == False: #While the player is still alive
        room, enemy = next_step(first_time)
        first_time = False
        if room == "quit":
            break
        enemy_name = enemy["name"] #Populating enemy name
        enemy_health = int(enemy["health"]) #Populating enemy health
        enemy_attack = int(enemy["attack"]) #Populating enemy attack rating
        print("You are in a " + room[0] + " " + room[1] + " room.\nYou're facing a: " + enemy_name + "\nEnemy health: " + str(enemy_health) + "\nEnemy attack rating: " + str(enemy_attack))#Description of room
        health = combat(health, attack, enemy_name, enemy_health, enemy_attack) #Begin combat. We only need health variable back.
        dead = death(health)



main()
