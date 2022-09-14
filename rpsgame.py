'''
RPS - ROCK, PAPER, SCISSORS 
@version: 1.2
@author: Johan Wrangö
@date: 2022-09-02
@description: A nice game against a super-AI RPS-player.
'''

import os
import random
import time
from rps_functions import gesture, get_hand, splash_screen
from colors import bcolors
from msvcrt import getwch

os.system('cls')

print(bcolors.YELLOW)
splash_screen("START")

wins = 0
losses = 0
plays = 0
keys = ['Q', '0', '1', '2', 'R', 'S', 'P'] 

while True:
    print(bcolors.YELLOW + "___________________________________")
    print("(R)ock, (P)aper, (S)cissors: ")

    while True:                             # Check keystrokes
        key_stroke = getwch().upper() 
        
        if key_stroke == "Q":                 # Quit game
            print(bcolors.YELLOW, end="")
            splash_screen("QUIT")
            print(bcolors.ENDC)                 # Restore default system colors
            time.sleep(2)
            exit()

        if key_stroke in keys:
            break
        

    ai_select = random.randint(0, 2)
    human = get_hand(key_stroke)
    ai = get_hand(str(ai_select))

    os.system('cls')

    plays += 1

    print("The AI chose:", end="")
    gesture(ai)
    print("You chose:", end="")
    gesture(human)

    if ai == human:
        print(bcolors.CYAN + bcolors.BOLD + "IT'S A TIE" + bcolors.ENDC)
    elif human == "ROCK":
        if ai == "SCISSORS":
            print(bcolors.GREEN + bcolors.BOLD + "YOU WON!" + bcolors.ENDC)
            wins += 1
        else:
            print(bcolors.FAIL + bcolors.BOLD + "YOU LOST" + bcolors.ENDC)
            losses += 1
    elif human == "PAPER":
        if ai == "ROCK":
            print(bcolors.GREEN + bcolors.BOLD + "YOU WON!" + bcolors.ENDC)
            wins += 1
        else:
            print(bcolors.FAIL + bcolors.BOLD + "YOU LOST" + bcolors.ENDC)
            losses += 1
    elif human == "SCISSORS":
        if ai == "PAPER":
            print(bcolors.GREEN + bcolors.BOLD + "YOU WON!" + bcolors.ENDC)
            wins += 1
        else:
            print(bcolors.FAIL + bcolors.BOLD + "YOU LOST" + bcolors.ENDC)
            losses += 1
    print(f"Wins: {str(wins)} | Losses: {losses} | Turns: {plays}")
