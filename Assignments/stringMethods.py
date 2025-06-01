# Garrett Knight
# GenSparkAI
# Assignment: Exploring String Methods

print("\n\t\t--Exporing String Methods --") # Project Title

# Task 1 - String Slicing and Indexing
print("\nTask 1 - Slicing and Indexing\n")
statement = "Python is amazing!" # String Variable
print(statement)
slice = statement[0:6] # 'Python'
print("\nFirst Word: " + slice)
backslice = statement[9:17]# 'Amazing'
print("Amazing part:" + backslice)
reverse_it = statement[::-1] # '!gnizam si nothyP'
print("Reverse statement: " + reverse_it)

# Task - 2 String Methods
print("\nTask 2 - String Methods\n")
greeting = " hello, python world! "
print(greeting, "\t# Regular print") # Regular print
print(greeting.strip(), "\t# strip() method") # Unwanted spaces removed
cap = greeting.strip() # Stripped greeting
print(cap.capitalize(), "\t# capitilize() method") # 'Hello, python world!'
neword = cap.capitalize() # Capitilize first letter
print(neword.replace("world", "universe"), "# replace() method") # 'Hello, python universe!'
print(cap.upper(), "\t# upper() method") # 'HELLO, PYTHON WORLD!'
bigcap = neword.replace("world", "universe") # The replacement
print(bigcap.upper(), "# upper() and replace() method") # 'HELLO, PYTHON UNIVERSE!'

# Task 3 - Check for Pa\\ttlindromes
print("\nTask 3 - Check for Palindromes\n")
word = input("Enter a word: ") # Prompts user to enter a word
palindrome = word[::-1] # User's input spelled backwards
# Gets rid of spacing in potential palindrome phrases
result = "".join(palindrome.split()) 
Input = "".join(word.split())
# If statement to check if user's input is a palindrome
if Input.lower() == result.lower(): # lower.() is to solve the case sensitivity
    # Displays if 'word' is a palindrome
    #word.strip() == palindrome.strip()
    print("\nYes, " + word + " is a palindrome!✅")
else:
    # Displays if 'word' is not a palindrome
    print("\nNo, " + word + " is not a palindrome.❌")
print()
