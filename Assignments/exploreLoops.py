# Garrett Knight
# Assignment: Explore Loops in Python
# GenSparkAI
# 05/10/2025

# Task 1 - Counting Down with Loops

print("\n- Counting Down with Loops -")
i = int(input("\nEnter Countdown Number: "))# Prompts the user to enter starting number
print()# Extra space betweem lines

# While loop to print numbers from user input counting down to 1
while i >= 1:
    print(i, end = "- ")
    if i == 1:
        print("🚀 Get Ready For Lift Off!")
        break # To prevent else statement from executing. 
    i -= 1
else:
    #if i <= 0:
    print("Error! Countdown must be positive.")  

# Task 2 - Multiplication Table with for Loops

print("\n- Multiplication Table with for Loops -")
j = int(input("\nEnter a number: "))# Asks the user to enter number
print()
# Prints a for loop of a multiplication table for input from 1 through 10
for k in range(1, 11):
    if k == 5: # Organizing the rows and columns of table
        print("[", j, "x", k, "=", j * k, end = " ],\n\n")
    elif k == 10:
        print("[", j, "x", k, "=", j * k, end = " ]}\n")
    elif k == 1:
        print("{[", j, "x", k, "=", j * k, end = "],\t")
    else:    
        print("[", j, "x", k, "=", j * k, end = " ],\t")

# Task 3 - Find the Factorial

print("\n- Find the Factorial -")
num = int(input("\nInput n!: "))# Prompts the user to enter factorial number

factor = 1
if num < 0: # Displays if user enters a negative number
    print("\nError! Negative numbers do not have factorials.")
elif num == 0: # Displays if 0 is entered
    print("\nThe factorial of", num, "is 1.")
else:
    # Calculates factorial of entered number
    for x in range(1, num + 1):
        factor =  factor * x 
    print("\nYour entry of", num, "\b! =", factor, "\b.")
print()       
   
    