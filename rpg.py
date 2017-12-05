import action
import equipment
import enviroment
import json
import random

def main():
    health = 100 #User's health
    attack = 10 #User's attack strength
    first_time = True
    dead = False #If the user is dead, change to True
    while dead == False: #While the player is still alive
        enviroment.generator("0","0")
        room, enemy = action.next_step(first_time)
        first_time = False
        if room == "quit":
            break
        enemy_name = enemy["name"] #Populating enemy name
        enemy_health = int(enemy["health"]) #Populating enemy health
        enemy_attack = int(enemy["attack"]) #Populating enemy attack rating
        print("You are in a " + room[0] + " " + room[1] + " room.\nYou're facing a: " + enemy_name + "\nEnemy health: " + str(enemy_health) + "\nEnemy attack rating: " + str(enemy_attack))#Description of room
        health = action.combat(health, attack, enemy_name, enemy_health, enemy_attack) #Begin combat. We only need health variable back.
        dead = action.death(health)



main()
