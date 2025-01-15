"""
This is a simple Number Guessing Game.
The program generates a random number between 1 and 100, and the user is tasked with guessing it.

Features:
- Provides feedback if the user's guess is too high or too low.
- Displays a congratulatory message when the correct number is guessed.
- Utilizes the colorama library for colorful and engaging output.

How it works:
1. The program generates a random number using Python's random module.
2. The user enters their guess in an infinite loop until they correctly guess the number.
3. Feedback is given for each guess, and the game ends once the correct number is guessed.
"""

import random
from colorama import Fore, Back, Style

print(Style.BRIGHT + "\nNUMBER GUESSING GAME" + Style.RESET_ALL)

r1 = random.randint(1,100) #Generates a random number between 1 and 100

print(Fore.GREEN + "\nA number between 1-100 has been generated." + Style.RESET_ALL)

while True:
    #User is asked to give input
    r2 = int(input(Fore.CYAN + "\nMake your guess: " + Style.RESET_ALL))

    if r1<r2: #Displays if guess is higher than the random number
        print(Fore.RED + "\nYour guess is too high!" + Style.RESET_ALL)
    elif r2<r1: #Displays if random number is higher than what the user guessed
        print(Fore.RED + "\nYour guess is too low!" + Style.RESET_ALL)
    else: #If the user has guessed correctly (r1==r2)
        print(Back.LIGHTBLUE_EX + f"\nCorrect! The random number generated is {r1}" + Style.RESET_ALL)
        print("\n")
        break
