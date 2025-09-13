#4. Build a Number Guessing Game (random number 1–100, user keeps guessing until correct).

import random
def guessNumber():
    guessNum = random.randint(1,100)
    # guessNum = 34
    inputnum = 0
    attempts = 0
    print("WELCOME TO NUMBER GUESSING GAME")
    print("GUESS A RANDOM NUMBER BETWEEN 1-100") 
    while inputnum!=guessNum:
        inputnum = int(input("Enter your guess:"))
        attempts += 1
        if inputnum > guessNum:
            print("Too High , Try Again!!")
        elif inputnum < guessNum:
            print("Too Low , Try Again!!")
        else:
            print(f"You Guessed Right! The number was {guessNum}.")
            print(f"Attempts taken: {attempts}")
guessNumber()

