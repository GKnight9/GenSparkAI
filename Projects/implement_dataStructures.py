# Garrett Knight
# GenSparkAI  
# Project: Implement Your own Data Structures

inventory = {} # This is the dictionary of the inventory list.
#Title
print("\nWelcome to the Inventory Manager!") 
# print(inventory)"apple": (10, 2.50), "banana": (20, 1.20), "mango": (15, 3.00)
#inventory["apple"] = (8, 2.55) 
x = 0
while x >= 0: # While loop to prompt the user to modify inventory.
    # This was added to display the inventory list only when I want it to.
    def display_inv(inventory):
        # These are the total quantity of the items and their total price. 
        total_quantity = 0
        total_value = 0.0  
        # For loop is to display the inventory list by their keys and values in rows.
        for item, (quantity, price) in inventory.items():
            total_quantity += quantity
            total_value += quantity * price 
            price_value = quantity * price
            # This is to print the inventory list the way I want it
            new_list = (f"Item: {item}, Quantity: {quantity}, Price: ${price}, Total Value: ${"%.2f"%price_value }")
            print(new_list)
        # Displays item totals
        print(f"Total Quantity: {total_quantity}")
        print(f"Total Inventory Value: ${"%.2f"%total_value }" )
    # Prompts the user to select an option    
    print("\nWould you like to: ")
    print("\n1. Add Item\t2.Remove Item\t3. Update Item\t4. View Inventory\t0. Exit")
    action = int(input("Please select option: "))
    print()
    if action == 1: # Promots the user to add an item to the list
            addItem = input("Enter new item to add: ")
            addQuantity = input("Enter quantity: ")
            addPrice = input("Enter price: ")
            inventory[addItem] = (int(addQuantity), float(addPrice)) # Adding a new item to the inventory.
            print("Updated Inventory: ")
            display_inv(inventory)
            print("Added item: ", addItem)
    
    elif action == 2: #Prompts the user to romove an item from the inventory.
            removeItem = input("Select item to delete: ")
            del inventory[removeItem] # Removing an item from the inventory.
            print("Updated Inventory: ")
            display_inv(inventory)
            print("Removed item: ", removeItem)
    
    elif action == 3: # Prompts the user to change the quantity and/or the price of selected item.
            changeValue = input("Select Item to update: ")
            changeQuantity = int(input("Enter Quantity: "))
            changePrice = input("Enter price: ")
            inventory[changeValue] = (changeQuantity, float(changePrice))
            print("Updated Inventory: ")
            display_inv(inventory)
            #print(inventory)
    elif action == 4: # Displays the current inventory
          print("Current Inventory: ")
          display_inv(inventory)
    elif action == 0: # Prompts the user to exit the loop and close the program
        print("Goodbye!")
        break
    else: # Displays if user enters a number outside of the 0, 4 range
            print("Error: Please enter 0-4")
            
print()