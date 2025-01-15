"""
This is a simple Calculator program.
It allows users to perform basic arithmetic operations such as:
- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero).

The program accepts two numbers as input and allows the user to choose an operation
from a menu. It then displays the result in a styled output using the colorama library.
"""

from colorama import Fore, Back, Style

print(Style.BRIGHT + "\nC A L C U L A T O R" + Style.RESET_ALL)

#Taking the first two numbers from the user
n1 = int(input(Fore.RED + "\nEnter the first number: " + Style.RESET_ALL))
n2 = int(input(Fore.RED + "\nEnter the second number: " + Style.RESET_ALL))

#Giving a small menu to choose what to do with the numbers
print("\nChoose one of the following:")
print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
ch = int(input(Fore.RED + "\nEnter your choice: "))

#After the choice is made, it goes through if-else statements
if ch == 1: #This statement adds the two numbers
    print(Fore.CYAN + f"\n{n1} + {n2} = {n1 + n2}" + Style.RESET_ALL)
    print("\n")
elif ch == 2: #This statement subtracts the two numbers
    print(Fore.CYAN + f"\n{n1} - {n2} = {n1 - n2}" + Style.RESET_ALL)
    print("\n")
elif ch == 3: #This statement multiplies the two numbers
    print(Fore.CYAN + f"\n{n1} X {n2} = {n1 * n2}" + Style.RESET_ALL)
    print("\n")
elif ch == 4: #This statement divides the two numbers
    if n2==0:
        print(Fore.CYAN + "\nDivision by zero is not possible!") #Gives out zero error if denominator is zero
        print("\n")
    else:
        print(Fore.CYAN + f"\n{n1} ÷ {n2} = {n1 / n2}" + Style.RESET_ALL)
        print("\n")
else: #If number chosen is not between 1-4
    print(Back.YELLOW + "\nInvalid choice" + Style.RESET_ALL)
    print("\n")
