# -*- coding: utf-8 -*-

import random


currentLoop = "current loop: "

currentNumber = 0
currentGuess = -1
playing = bool(False)
playerScore = int(input("How many guesses would you like to play with?: "))
gameRangeMin = int(input("Enter the game's lowest number to guess from: "))
gameRangeMax = int(input("Enter the game's highest number to guess to: "))  


if(gameRangeMin < gameRangeMax):
    currentNumber = random.randint(gameRangeMin, gameRangeMax)
    while playing != True:
        currentGuess = input ("Enter a guess between " + str(gameRangeMin) + " and " + str(gameRangeMax) + ": ")
        if(playerScore == 0):
            print("You're all out of tries, sorry.")
            print("The number you were trying to guess was: " + str(currentNumber))
            break
        if(int(currentGuess) == currentNumber):
            print("You guessed correctly!")
            print("Your score was: " + str(playerScore))
            
            choice = input("Do you want to play again? ")
            playing = False
            if(choice == "yes" or choice == "y" or choice == "Yes"):
                playing = False
                playerScore = int(input("How many guesses would you like to play with?: "))
                gameRangeMin = int(input("Enter the game's lowest number to guess from: "))
                gameRangeMax = int(input("Enter the game's highest number to guess to: "))  
                currentNumber = random.randint(gameRangeMin, gameRangeMax)

            else: 
                playing = True
            
        else:
            if(int(currentGuess) > currentNumber):
                print("Your guess was too high. Try guessing lower.")
            else: 
                print("Your guess was too low. Try guessing higher.")
            print("You guessed incorrectly, please guess again.")
            print("")
            print("Current player score is: " + str(playerScore))
            playerScore -= 1 
else:
    print("Your min number was greater than your max number. Please try again.")
    quit()

    
    
    