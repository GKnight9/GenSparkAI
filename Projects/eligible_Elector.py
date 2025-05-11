# Garrett Knight
# GenSparkAI 
# Project: Eligible Elector
# 05/08/2025

print("\n\t\t\t" + "-" * 10 + "Eligible Elector" + "-" * 10)# Title of the project

age = int(input("\nWelcome potential voters. Please enter your age: "))# Prompts the user to enter their age.
print()#Add space between lines
# Depending on the user's input, certain messages will display.
if(age >= 18):
    # If the user is 18 or older, this message will display.
    print("Congratulations, you are eligible to vote.😁 Get out and make your voice heard!")
elif(age == 17):
# I added this line so the year would not show up as plural if they were only 1 year behind.
    print("Oops! You have 1 year left until you're eligible!🤣")
elif(age < 0):
 # Displays if user enters a negative number.   
    print("Invalid Entry!🤖 Please enter a whole number.")
else:
# If the user enters less than 18, this message will tell the user how many years they have to wait.
    print("Sorry, you're not eligible yet. You have", 18 - age, "more years to wait.😒")
print()