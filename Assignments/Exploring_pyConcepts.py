#Garrett Knight
#genai_externship
#Assignment: Exploring Python Concepts

#Task 1 - Variables: Your First Python Intro
print("\n" + "*" * 3 + "Task 1 - Variables: Your First Python Intro" + "*" * 3 + "\n")
name = "Bob"
age = 23
age = int(age)
height = 6.10
height = float(height)
print("Meet " + name + ", a", age, "year old Computer Science major standing at around", 
      height, "feet tall.")

#Task 2 - Operators: Playing with Numbers
print("\n" + "*" * 3 + "Operators: Playing with Numbers" + "*" * 3 + "\n")
num1 = 9
num2 = 3
print("9 plus 3 is", num1 + num2)
print("9 minus 3 equals", num1 - num2)
print("Multiply 9 by 3 and you get", num1 * num2)
print("Finally, 9 divided by 3 is", num1 / num2)

#Task 3 - Conditional Statements: The Number Checker
print("\n" + "*" * 3 + "Conditional Statements: The Number Checker" + "*" * 3 + "\n")
num0 = input("Enter a number: ")
num0 = int(num0)
print()
if(num0 < 0):
    print(num0, "is a negative integer.")
elif(num0 == 0):
    print(num0, "is a perfect balance!")
else:
    print(num0, "is a positive integer.")
print()