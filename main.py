import os
import random

version = 2.0
os.system("title Guessing Game !!")
os.system("color 02")

i = 1
while i < 100:

    answer = int(input("\n\n\n\n\n\n\n\nGuess a number beetween 1-5 :"))
    RandomNumber = random.randint(1, 5)

    if answer == RandomNumber:
        print("You have won !!")

    else:
        print("You have lost")
        print("Random number was ", RandomNumber)
        i = i + 1
