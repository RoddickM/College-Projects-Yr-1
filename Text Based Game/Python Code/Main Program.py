import random as rnd
import time
monster_name_list = ["Giant Rat", "Goblin Warrior", "Grim Lock"]
hp = rnd.randrange(4, 13) + 10
strength = rnd.randrange(3, 8)


def fight(player_name, monster_name, player_str, monster_str, monster_hp):
    while True:
        global hp
        player_attack = player_str + rnd.randrange(1, 7)
        monster_hp -= player_attack
        print("Player is attacking")
        time.sleep(1.5)
        print(monster_name, "has lost", str(player_attack) + " hp")
        time.sleep(1.5)
        print(monster_name, "hp:", monster_hp)
        time.sleep(1.5)

        if monster_hp <= 0:
            break
        elif hp <= 0:
            return hp
        else:
            pass

        monster_attack = monster_str + rnd.randrange(1, 3)
        hp -= monster_attack
        print("\n" + str(monster_name), "is attacking")
        time.sleep(1.5)
        print(player_name, "has lost", str(monster_attack) + " hp")
        time.sleep(1.5)
        print(player_name, "hp: " + str(hp) + "\n")
        time.sleep(1.5)

        if monster_hp <= 0:
            break
        elif hp <= 0:
            return hp
        else:
            pass

        hp += rnd.randrange(0, 5)


def show_stats(player_name_2):
    print(player_name_2, "hp:", hp)
    print(player_name_2, "str:", strength)


print("Wizard: Welcome to the dungeon, Challenger.")
time.sleep(1.5)
print("Wizard: Try not to die~")
time.sleep(1.5)
name = input("Wizard: What is your name challenger?: ")
show_stats(name)
for stats in range(0, 3):
    print("\n" + str(monster_name_list[stats]), "has appeared!")
    fight(name, monster_name_list[stats], strength, monster_str=((stats + 3) * rnd.randrange(1, 5)), monster_hp=((stats + 1) * 10))
    strength += rnd.randrange(3, 5)
    if hp <= 0:
        exit("GAME OVER!!")
    else:
        pass
    heal = input("\nDo you want to heal by 5pts?(Y/N): ")
    if heal.upper() == "Y":
        hp += 5
    else:
        pass
    print("\nCongratulations! You have defeated your foe!")
    show_stats(name)

    cont = input("\nDo you want to continue?(Y/N): ")
    if cont.upper() == "N":
        exit("GOOD BYE!!")
    else:
        pass

print("\nCongratulations! You have defeated the dungeon!")
print("Thank you for playing!")
print("GOOD BYE!!")
