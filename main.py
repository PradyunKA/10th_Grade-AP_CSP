# Pradyun Kotcherelakota
# AP Computer Science Principles
# Create Task
# 1/20/2022

# Import all modules necessary
import random
import colorama
from colorama import Fore


# First: Make a function where the computer will generate a random 4-digit number and store it to a variable: num.
# This is the number that the user must try and guess.
def create_num():
    num = random.randint(1111, 9999)
    print("\nA 4 digit number has been created for you to guess!")


# Then create a ready function that will tell the user the directions of the game and prompt him for a ready input.
ready = input(
    Fore.LIGHTCYAN_EX + "Welcome to the Number Guessing Game! The rules are very simple.\n You will receive a 4-digit number that you must attempt to guess within 10 tries.\n You will receive a black marker if the digit is in the number but not in the correct place, and you will receive a white marker if the digit is in the number and the right place. Ready to Play?: ")
if ready.lower() == 'yes':
    create_num()





