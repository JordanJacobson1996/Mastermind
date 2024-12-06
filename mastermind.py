import random

#Generates random code based on the six letters available.
code = "".join(random.sample('ABCDEF', 4))
numGuesses = 0
board = "" #For displaying the correct pegs for the guesses, black for correct letter and position and white for letter in code.

guess = input("Please enter your first guess, must be four letter from ABCDEF and have no repeated letters:  ").upper()

while len(guess) > 4:
    print("You have entered too many letters, please try again")
    guess = input("Please enter a guess: ")

#Main loop that iterates through 12 guesses or ends if the player gets the code correct.
while numGuesses < 12:
#Loop to check positions of guess letters against code letters and add results to board.
    i = 0
    board = ""
    while i < len(guess):
        if guess[i] == code[i]:
            board = board + "B"
        elif guess [i] in code:
            board = board + "W"
        else:
            board = board + "X"
        i += 1
    numGuesses += 1
    print(guess)
    print(board)

    #Checks if player has won or lost.
    if board == "BBBB":
        result = 'The code was ', code, '. The player guessed it in ', numGuesses, ' guesses.'
        break
    elif numGuesses == 12:
        result = "Player failed to guess the code. The code was ", code
        break
    guess = input("Guess incorrect, make another guess: ")

print(result)