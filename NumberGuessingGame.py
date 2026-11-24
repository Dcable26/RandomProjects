from collections import UserDict
import random
from xml.dom import UserDataHandler




def TestingNumber(theNumber):
    #For testing Reveal the guessed number

    print(f'The number picked is: ',theNumber)
    print()
    print()


def WelcomeScreen():
    print(f'Thank you for playing the number guessing game!')
    print(f'Here are the rules:')
    print(f'1. The number is between 1-1000')
    print(f'2. After every guess you will be told if your guess was higher or lower then the number')
    print(f'3. Your prevous guess and number of guesses will be displayed in the "Previously guessed" section when you are done')
    print(f'Good Luck and have fun!')
    print()
    print()
    userResponse = input(f'Press Enter to continue')

    if userResponse == "anything":
        print("haha...")



def EndGameScreen(previousGuesses, theNumber):
    print(f'\n\n\n\nCongrats you guessed the correct number!')
    print(f'\nHere are your stats:')
    print(f'The correct number was {theNumber}')
    print(f'Number of guesses taken: {len(previousGuesses) + 1}')
        
    


def GameStage(previousGuesses):


        print("\n\n\n\n Previous Guesses:")








def main():

    #Set variables
    theNumber = random.randint(1,1000)
    runGame = True
    userGuess = 0
    previousGuesses = []

    #TestingNumber(theNumber)


    #Display Welcome Screen
    WelcomeScreen()
    print("\n\n\n\n\n\n\n")
    
    while runGame == True:
        userGuess = input("Please enter a number from 1-1000: ")

        #Validate input
        while (userGuess.isdigit() == False) or int(userGuess) < 1 or int(userGuess) > 1000:
             print(f"Sorry {userGuess} is not a valid input")
             userGuess = input("Please enter a number from 1-1000: ")
        
          
        userGuess = int(userGuess)


        #Adds the previous guesses to list
        if userGuess < theNumber:
            previousGuesses.append(f'{userGuess} is Lower')
        elif userGuess > theNumber:
            previousGuesses.append(f'{userGuess} is Higher')
        else:
            runGame == False
            EndGameScreen(previousGuesses, theNumber)
            break

        for index, value in enumerate(previousGuesses):

            if index == len(previousGuesses)-1:
                print(f'{value}\n')
                break

            print(value, end=",")
    
     
    




#Calls main
if __name__ == '__main__':
    main()
