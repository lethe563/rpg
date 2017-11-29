def combat(health, enemy_health, attack, enemy_attack):
    while health > 0 and enemy_health > 0:
        command = input("Do you wish to attack? (y/n)")
        if command == "y":
            enemy_health -= attack
            health -= enemy_attack
            print("Success!\nYour health is now: " + str(health) + "\nYour enemy's health is now: " + str(enemy_health))
        elif command == "n":
            health -= enemy_attack
            print("Failure! Just press y next time.\nYour health is now: " + str(health) + "\nYour enemy's health is now: " + str(enemy_health))
        else:
            print("Please enter either y or n")



def main():
    health = 100
    enemy_health = 100
    attack = 10
    enemy_attack = 5

    combat(health, enemy_health, attack, enemy_attack)

main()
