# Garrett Knight
# GenSparkAI
# Project: Number Guessing Game
# 05/20/2025

# Using the random module to generate a random number between 1 and 100.
import random
number_to_guess = random.randint(1, 100)
j = 0 # Counts inputs in the while loop.
print()
print("-- " * 10, "Number Guessing Game", " --" * 10)# Title of the game.
# This is an introduction statement explaining the rules of the game.
print("\nWelcome to the Number Guessing Game! \nYour objective is to pick the correct random number between 1 "
"and 100 in 10 tries.\nGood luck!")
# While loop generates the number guessing game.
while j >= 0:
    # Prompts the user to guess a number.
    i = int(input("\nGuess the number: "))
    j += 1
    attempts = 10
    # These are the various results displayed depending on user's input.
    while i in range(1, 101):
        if i > number_to_guess:
            # Displays message if the number is too high.
            print("\nNope! Too high!   \nAttempts Remaining:", attempts - j)
            break
        elif i < number_to_guess:
        # Displays message if the number is too low.
            print("\nOops! To low!  \nAttempts Remaining:", attempts - j)
            break
           
        else:
        # Message displays if user guesses the right number.
            print("\nCongratulations! You guessed it in", j, "tries!\n")
            break
        
    else: # Displays if user enters a number outside of the range of 1 and 100.
        print("\nAh, snap! Number must be between 1 and 100.")
        print("Attempts remaining:", attempts - j)
    # Ends the while loop when the user guesses the right number.
    if i == number_to_guess:
         break
    if j == 10: # Limits number of attempts to 10.
            print("\nGame over! Better luck next time.\tNumber was:", number_to_guess, "\n")
            break