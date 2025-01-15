"""
This program generates a random password containing a mix of:
- Uppercase and lowercase letters
- Numbers
- Special characters (e.g., @, #, $, %, etc.)
"""

import random
import string
from colorama import Fore, Back, Style

def gen_pass(length):

    if length<8: #adding condition to meet password requirements
        print(Fore.RED + "\nMinimum 8 characters needed for a password!" + Style.RESET_ALL)
        print("\n")
    else:
        #defining character pools using string package
        letters = string.ascii_letters #ascii letters has all uppercase and lowcase letters
        digits = string.digits #digits include the numbers 0-9
        special_char = string.punctuation #punctuation includes special charcters !@#$%^&*()

        password = [
            #picking any of these randomly and adding it to the password list
            random.choice(letters),
            random.choice(digits),
            random.choice(special_char)
        ]

        all_char = letters + digits + special_char #combining all character pools
        #picking random characters from all_char and making sure it is the desired length
        password += random.choices(all_char, k = length - len(password))

        return ''.join(password) #converting password list into a single string

print(Style.BRIGHT + "\nPASSWORD GENERATOR" + Style.RESET_ALL)
#asking user to input the desired password length
length = int(input(Fore.LIGHTBLUE_EX + "\nEnter the length you want for your password: " + Style.RESET_ALL))
#calling the gen_pass function to print the final output
print(Fore.YELLOW + "\nGenerated Password: ", gen_pass(length) + Style.RESET_ALL)
print("\n")
