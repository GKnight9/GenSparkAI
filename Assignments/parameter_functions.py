# Garrett Knight
# GenSparkAI
# Assignment: About Parameters of Functions

# Task 1 - Writing Functions
name = input("\nPlease enter your name: ")
def greet_user(name):
    return (f"\nHello, {name}!")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))    
def add_numbers(a, b):
    return a + b
print(greet_user(name), "Welcome aboard! The sum of" , a, "and", b, "is" , add_numbers(a, b), "\b.")
#Task 2 - Using Default Parameters
pets = int(input("\nHow many pets do you have? "))
i = 0
while pets >= 1:
    
    pet_name = input("Enter pet name: ") # Prompts user to enter pet name
    animal_type = input(f"What kind of animal is {pet_name}? ", ) # Prompts user to enter what kind of animal it is
    
    i += 1
    if animal_type == "":
        animal_type = ("dog")
    def describe_pet(pet_name, animal_type):
        
            return(f"\nYou have a {animal_type} named {pet_name}.\n")
    print(describe_pet(pet_name, animal_type))
    if i == pets:
        break
# Task 3 - Functions with variable arguments
def make_sandwich(*args):
        ingredients = args 
        #Wprint(ingredients)
        print("Make a sandwich with the following ingredients: " + ingredients[0] + ingredients[1] + ingredients[2])
# The ingdredients stored in the sandwich       
make_sandwich("-Lettuce ", "-Onions ", "-Tomatoes ")
print()
# Task 4 - Understanding Recursion
n = int(input("Enter factorial number: ")) # Prompts user to enter factorial number
def factorial(n):

    if n == 1: # Base Case
        return 1
    
    else:
        
        return n * factorial(n - 1) # Recursive case
            
print("The factorial of", n, "is", factorial(n))
m = int(input("\nEnter fibonacci number: ")) # Prompts user to find nth number in fibonacci sequence
def fibonacci_recursion(m):
    a = 0
    b = 1
    if m <= 1:
         return m
        
         
    return fibonacci_recursion(m - 1) + fibonacci_recursion(m - 2)
# Generate Sequence
fibo_seq = fibonacci_recursion(m) 
#print(fibo_seq) # First m numbers of fibonacci sequence
print("The", m, "\bth number in the fibonacci sequence is", fibo_seq)
print()