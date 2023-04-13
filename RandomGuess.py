#RandomGuess.py

#import random for number guessing in the game
import random

#we have to generate random number between 1 and 15
#Defining main function
def main():
    random_number = random.randint(1,15)
    
#prompt the user to enter a number between 1 and 15, or 0 to quit
    guess_num = int(input("Enter a number between 1 and 15, or 0 to quit: "))

#keep asking for input until the user enters 0, which will prompt them to quit
    while guess_num != 0:
        if guess_num > random_number:
            print("Too high, try again")          
        elif guess_num < random_number:
            print("Too low, try again")
        else:
            print("Congratulations! you guessed the right number!")

#Generate new random number for the next game
            random_number = random.randint(1,15)
#Prompt the user to enter a number again, or 0 to quit
        guess_num = int(input("Enter a number between 1 and 15, or 0 to quit: "))

#if the user enters 0, the game gets terminated and thanks for playing
#message is displayed
    if guess_num == 0:
        print("Thanks for playing!")
        

#Calling main function
main()
