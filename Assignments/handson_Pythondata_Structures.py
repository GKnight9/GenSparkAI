# Garrett Knight
# GenSparkAi
# Assignment: Hands on Python Data Structures

# Task 1 - Working with Lists
print("\nTask 1 - Working with Lists")
fruitfavs = ["apple", "banana", "cherry", "grapes", "orange"] # List of fruits
print("\nOriginal Fruit List: ", fruitfavs) # Prints original list
fruitfavs.append("pear") # Adds new fruit to the list
print("After adding a new fruit: ", fruitfavs) # Print list with new item added
fruitfavs.remove("banana") # Removes item from the list
print("After removing a fruit: ", fruitfavs) # Prints list with item removed
fruitfavs.reverse() # Prints the list with the items listed from backwards to forward
print("Reversed Fruit List: ", fruitfavs)
print()
# Task 2 - Exploring Dictionaries
print("Task 2 - Exploring Dictionaries\n")
myprofile = {"Name: ": " Terrag", "Age: ": "  24", "City: ": "  Salt Lake City"} # My profile
#print(myprofile)
myprofile["Favorite Color: "] = "Turqoise" # Adds new key to the dictionary
#print(myprofile)
myprofile["City: "] = " Orlando" # Changes value of key
#print(myprofile)
print("Keys \tValues") # These are to list the columns of keys and their values
print("----    ------")
for x in myprofile: 
    # This is to print all keys and values using a loop
    print( x, myprofile[x]) 
# Task 3 - Using Tuples
print("\nTask 3 - Using Tuples\n")
myfavs = ("Lawrence of Arabia", "1812 Overture", "Ringworld") # My tuple list
print("My favorite things: ", myfavs)
# Tempory converting tuple to a list to prevent error message
newfav = list(myfavs)
newfav[0] = "Who's Harry Crumb?"
# I have been modifying the if statement to confirm that tuples are immutible
if myfavs == tuple(newfav):
            print(myfavs)
else:
        print("Oops! Tuples don't change.")
tuple_length = len(myfavs) # To count the length of the tuple
print("Tuple length at", tuple_length, "\b.")
print()