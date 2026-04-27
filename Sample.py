
"""
Creating Python Programs: Module 3 & Part 1

Write a program that calculates the total amount of a meal purchased at a restaurant. 
The program should ask the user to enter the charge for the food and then calculate the amounts with
an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.

"""
try:
    # Get user input
    food_charge = float(input("Enter the charge for the food: $"))

    # Set predefined values
    tip_percent = 0.18
    tax_percent = 0.07

    # Perform calculations
    tip_price = food_charge * tip_percent
    tax_price = food_charge * tax_percent
    total_price = food_charge + tip_price + tax_price

    # Display results
    print("\n***** RESTAURANT RECEIPT *****")
    print(f"*    Food Charge: ${food_charge:.2f}     *")
    print(f"*      Tip (18%): ${tip_price:.2f}      *")
    print(f"*       Tax (7%): ${tax_price:.2f}      *")
    print("------------------------------")
    print(f"*    Total Price: ${total_price:.2f}     *")
    print("------------------------------")
   
except ValueError:
    print("Error: Please enter a valid numeric value for the food charge.")