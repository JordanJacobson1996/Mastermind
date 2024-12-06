import random

#Generates random code based on the six letters available.
code = "".join(random.sample('ABCDEF', 4))
numGuesses = 0
board = "" #For displaying the correct pegs for the guesses, black for correct letter and position and white for letter in code.

guess = input("Please enter your first guess, must be four letter from ABCDEF and have no repeated letters:  ").upper()

while len(guess) > 4:
    print("You have entered too many letters, please try again")
    guess = input("Please enter a guess: ")

#Loop to check positions of guess letters against code letters and add results to board.
i = 0
while i < len(guess):
    if guess[i] == code[i]:
        board = board + "B"
    elif guess [i] in code:
        board = board + "W"
    else:
        board = board + "X"
    i += 1

print(code)
print(guess)
print(board)

