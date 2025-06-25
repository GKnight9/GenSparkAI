# Garrett Knight
# GenSparkAI
# Project: About Menu

print("\nWelcome to the Recursive Artistry Program!") # Title
# Menu of Recursive Functions
x = 0
while x >= 0:
    # Prompts user to select an option
    print("\nPlease choose from the following: ")
    print("\n1. Calculate the factorial of a number")
    print("2. Find the nth number of a Fibonacci number")
    print("3. Draw a recursive factoral pattern: ")
    print("4. Exit")
    select = int(input("\n\tEnter Here: "))
    # Case 1 - Prompts user to enter a number and find is factorial
    if select == 1:
        n = int(input("\nEnter factorial number: "))
        def factorial(n):
            if n == 1:
                # Base case
                return 1
            elif n == 0:
                # If user enters 0
                return 1
            elif n < 0:
                # If user enters negative number
                print("\nOops! Negative numbers don't have factorials.")
            else:
            # Recursive Case
                return n * factorial(n -1)
        print("\n\tThe factorial of", n, "is", factorial(n), "\b.")
    # Case 2 - Prompts the user to find the nth number in the Fibonacci Sequence
    elif select == 2:
        m = int(input("\nEnter Fibonacci number: "))
        def fibonacci_recursion(m):
            if m == 1:
               return m
            elif m == 0:
                return 0
            elif m < 0:
                
                print("\nOoof! Fibonacci numbers can't be negative.")
                return 0
            else:
                return fibonacci_recursion(m - 1) + fibonacci_recursion(m - 2)
        print("\n\tThe", m, "\bth number in the Fibonacci Sequence is", fibonacci_recursion(m), "\b.") 
    # Case 3 - Fractoral Pattern
    elif select == 3:
        import turtle
        # Create turtle screen
        screen = turtle.Screen()
        screen.bgcolor("lightblue")
        

        def tree(plist, l, a, f):
            # plist is list of pens
            # l is length of branch
            # a is half of the angle between 2 branches
            # f is factor by which branch is shortened from level to level.
            if l > 5:
                lst = []
                for t in plist:
            
                    t.forward(l)
                    s = t.clone()
                    t.left(a)
                    s.right(a)
                    lst.append(t)
                    lst.append(s)
                tree(lst, l * f, a, f)
        
        
        def main():
            t = turtle.Turtle()
            t.shape("turtle")
            t.color("green")
            t.pensize(5)
            # Makes the tree look nicer
            t.hideturtle()
            t.speed(100)
            t.left(90)
            t.penup()
            t.goto(0, -200)
            t.pendown()

            j = tree([t], 200, 65, 0.6)
        main()
        screen.exitonclick()
    # Case 4 - Ends the program
    elif select == 4:
        print("\nGood Bye!")
        print()
        break
    else:
        # Error message if user inputs wrong number
        print("\nInput Error: Please enter 1 -4.")       
