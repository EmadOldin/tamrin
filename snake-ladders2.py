import time
import random
from colorama import Fore

SNAKESANDLADDERS = {
    27: 7,
    35: 5,
    39: 3,
    50: 34,
    59: 46,
    66: 24,
    73: 12,
    76: 63,
    89: 67,
    97: 86,
    99: 26,
    2: 23,
    8: 29,
    22: 41,
    28: 77,
    30: 32,
    44: 58,
    54: 69,
    70: 90,
    80: 83,
    87: 93,
}


n = int(input("Enter how many players want to play : "))
player_position = [0] * n
player_start = [0] * n


def tas():
    return random.randint(1, 6)


a = True
while a:
    for i in range(len(player_position)):
        x = tas()
        if x == 6 and player_position[i] == 0:
            print(Fore.YELLOW, f"user {i+1} start the game")
            player_start[i] = 1

        elif player_start[i] == 1:
            player_position[i] = player_position[i] + x
            time.sleep(0.5)
            if player_position[i] == 100:
                print(Fore.GREEN, f"user {i+1} is winner")
                a = False
                break

            elif player_position[i] in SNAKESANDLADDERS:
                y = player_position[i]
                player_position[i] = SNAKESANDLADDERS[player_position[i]]
                print(Fore.CYAN, f"user {i+1} go from {y} to {player_position[i]}")
            elif player_position[i] > 100:
                player_position[i] = player_position[i] - x
            print(Fore.WHITE, f"user {i+1} position = {player_position[i]}\n")
            # continue
        else:
            continue
