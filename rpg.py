import action
import equipment
import enviroment
import interface
import json
import random

def main():
    current_x = 0
    current_y = 0
    health = 100.0 #User's health
    attack = 10 #User's attack strength
    first_time = True
    continue_quest = True
    dead = False #If the user is dead, change to True
    while dead == False: #While the player is still alive
        if first_time == True:
            continue_quest = interface.initial()
            first_time = False
        if continue_quest == False:
            print("Goodbye")
            break
        enviroment.generator(current_x, current_y)
        #room_number, room_size, room_material, enemies, number_of_enemies = enviroment.current_room(current_x, current_y)
        interface.room(current_x, current_y, health, attack)

        #print("x = " + str(current_x) + " y = " + str(current_y) + "\nEnemy:\t\t" + enemy_name + "\t\tYou:\nHealth\t\t" + str(enemy_health) + "\t\t\t" + str(health) +"\nAttack rating\t" + str(enemy_attack) + "\t\t" + str(attack))
        #print("You are in a " + room_size + " " + room_material + " room.\nYou're facing a: " + enemies["1"]["name"] + "\nEnemy health: " + str(enemies["1"]["health"]) + "\nEnemy attack rating: " + str(enemies["1"]["attack"]))#Description of room
        #health = action.combat(health, attack, enemies, room_number) #Begin combat. We only need health variable back.
        dead = action.death(health)



main()
