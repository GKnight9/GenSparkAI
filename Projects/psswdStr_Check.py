# Garrett Knight
# GenSparkAI
# Project: Password Strength Checker

import re
# Evaluate the Password
i = 0
while i >= 0: # Loops until user enters eligible password
    
    checklist = 10 # Evaluates the strength of password
    password = input("\nCreate a Password: ") # Prompts the user to create a password
    print()
    digicheck = any(char.isdigit() for char in password) # This ensures password contains a number
    spec_chars = set("!@#$%^&*()_+[]{}|;:',.<>?/`~\\\"")
    contains = any(char0 in spec_chars for char0 in password) # Ensures password contains a special character
    length = len(password) # Counts the length of the password
    low_case = any(char1.islower() for char1 in password) # Ensures the password has a one lower case letter
    up_case = any(char2.isupper() for char2 in password) # Ensures the password has at least one upper case letter
    space = any(char3.isspace() for char3 in password)
    # A least of if statements listed as switch statements in Python
    if length < 8: # Case 1: If the password is less than 8 characters long
        print("Error: Password must be 8 characters!❌")
        checklist -= 1 
    # Case 2: If password fails to have at least one upper case letter
    if(up_case == False): 
        print("Error:  Password must contain at least one upper case letter.❌") 
  
        checklist -= 1 
    # Case 3: If password does not have at least one lower case letter
    if(low_case == False):
        print("Error: Password must contain at least one lower case letter.❌")
  
        checklist -= 1
    # Case 4: If the password does not contain at least one number
    if(digicheck is False): 
        print("Error: Password must contain at least one number.❌")
     
        checklist -= 1 
    # Case 5: If password seizes to have at least one special character
    if(contains == False): 
        print("Error: Password must contain at least one special character!❌")
    
        checklist -= 1
    # Case 6: If the password contains any spaces
    if(space == True):
        print("Error: Password must not contain empty spaces!❌")
        checklist -= 1
    # Case 7: User inputs absolutely nothing
    if password == "":
        print("Error: Password cannot be blank.❌")
        print("Error: Password must not contain empty spaces!❌")
        checklist -= 2
    # Case 0: If all the prerequisites are met    
    if checklist >= 10: 
        print("Password Created ✅")
        print("Password Strength: ", checklist, "\b/10")
        print("🟩" * checklist, " 🦾\n")
        break
    print("Password Strength: ", checklist, "\b/10") # Shows password strength rating out of 10
    # Displays a password strength meter based on rating
    if checklist <= 3:
        print("🟥" * checklist, "🏴‍☠️")
    elif checklist <= 7:
        print("🟧" * checklist, "😝")
    elif checklist <= 9:
        print("🟨" * checklist, "🤺") 
