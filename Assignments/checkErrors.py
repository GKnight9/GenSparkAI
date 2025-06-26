# Garrett Knight
# GenSparkAI
# Assignment: Check your Knowledge on Errors

x = 0
while x >= 0:
# Understanding Python Execptions    
    try:
        num = int(input("\nPlease Enter Number: "))
        result = 100/num
    except ValueError:
        print("\nValue Error: Entry must be valid number.")
        #print()
    except ZeroDivisionError:
        print("\nZero Division Error: Cannot divide by zero!")
        #print()
    else:
        print("\nAnd the result is", result, "\b!")
        print()
        break
# Exception Types
try: # IndexError

    fruits = ["apple", "banana", "grapes"]
    print(fruits[5])
# Index 5 does not exist in fruits because it has only 3 items    
except IndexError:

    print("IndexError: Index does not exist.")
try: #KeyError
    students = {"Alex": "Computer Science", "Alice": "Mathematics", "Tyler": "Computer Science"}
    print(students["Philip"]) # Dictionary does nor contain a student named Philip
except KeyError:
    
    print("KeyError: Key not found in dictionary.")
try: # TypeError
    string = "Hello" + 5
    print(string)
except TypeError:

    print("Invalid variable type combination.")
# Using try...except...else...finally
y = 0
while y >= 0:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter the second number: "))
        divident = num1/num2
    except ValueError:

        print("Please enter valid inputs.")
    except ZeroDivisionError:
        
        print("Error: Cannot divide by zero!")
    else:

        print(divident)
       
    finally:

        print("Goodbye!")
        break