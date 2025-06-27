# Garrett Knight
# GenSparkAI
# Project: Calculator with Exception Handling
import logging
# To keep track of errors made on a seperat file
logger = logging.basicConfig(filename = 'error_log.txt', level = logging.ERROR, format = "{asctime} - {levelname} - {message}", style="{",datefmt="%Y-%m-%d %H:%M")
print("\n\t\t--Welcome to the Python Calculator!--") # The title header
x = 0
while x >= 0: # Loops through menu until program is terminated
    # Input Validation
    try:
        # Menu Options
        print("\nSelect Options:")
        print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Logging Errors\n0. Exit")
        user_input = int(input("\tYour Entry:   "))
    
        if user_input == 1: # Case 1 - Addition
        
            firstnum = int(input("\nEnter first number:   "))
            secondnum = int(input("\nEnter second number:   "))
            result = firstnum + secondnum
            print(firstnum, "+", secondnum, "=", result)
        
        elif user_input == 2: # Case 2 - Subtraction
        
            firstnum = int(input("\nEnter first number:   "))
            secondnum = int(input("\nEnter second number:   "))
            result = firstnum - secondnum
            print(firstnum, "-", secondnum, "=", result)
        
        elif user_input == 3: # Case 3 - Multiplication
        
            firstnum = int(input("\nEnter first number:   "))
            secondnum = int(input("\nEnter second number:   "))
            result = firstnum * secondnum
            print(firstnum, "*", secondnum, "=", result)
        
        elif user_input == 4: # Case 4 - Division
            try:

                firstnum = int(input("\nEnter first number:   "))
                secondnum = int(input("\nEnter second number:   "))
                result = firstnum/secondnum
            
            except ZeroDivisionError:
                # Displays if user divides by 0
                logging.error("Uh-oh! The ZeroDivisionError occured!") # Goes to text file
                print("OOPS! Division by zero is not allowed! Try again.")
           
            else:
                # If both numbers are above zero
                print(firstnum, "/", secondnum, "=", result)
        
        elif user_input == 5: # Case 5 - Dispalys the errors list recorded on error_log.txt
            
            f = open("error_log.txt", "r")
            print("\nError Log: ")
            print(f.read()) # Prints file to console
            
        elif user_input == 0: # Case 4 - Exit Program
            
            print("\nProgram Terminated!")
            print()
            break
        
        else:
            # Displays if user enters invalid number
            print("Error: Imput must be 0-5.")
    
    except ValueError:
        # If user inputs non integer value
        logging.error("Uh-oh! The ValueError occured! ") # Goes to text file
        print("ValueError: Entry must be a valid number!") 



  