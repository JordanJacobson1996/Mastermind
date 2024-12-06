import random

#Generates random code based on the six letters available.
code = "".join(random.sample('ABCDEF', 4))
numGuesses = 0

guess = input("Please enter your first guess, must be four letter from ABCDEF and have no repeated letters:  ").upper()

while len(guess) > 4:
    print("You have entered too many letters, please try again")
    guess = input("Please enter a guess: ")

print(guess)
