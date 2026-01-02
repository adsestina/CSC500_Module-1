# Importing decimal for more precise monetary calculations
from decimal import Decimal

# Menu dictionary
menu = {
    "fried ravioli": Decimal(9.99),
    "ceaser salad": Decimal(8.99),
    "fettuccine alfredo": Decimal(18.99),
    "ribeye steak": Decimal(38.99),
    "tiramisu": Decimal(9.99),
    "house chanti": Decimal(10.00),
    "soda": Decimal(2.99)
}

# For fun, giving user option to add item from menu or enter food total
print("\nOptions:")
print("1. Select your items from the menu")
print("2. Enter total food cost manually")

food_total = Decimal(0.0)

# Validate user option
while True:
    choice = input("\nEnter 1 or 2: ")
    if choice == "1" or choice == "2":
        break
    else:
        print("Invalid selection. Please enter 1 or 2.")

if choice == "1":
    print("Menu:")
    for item, price in menu.items():
        print(f"- {item.title()}: ${price:.2f}")
    print("\nEnter menu items one at a time.")
    print("Type 'done' when finished.\n")

    while True:
        item_choice = input("Enter food item: ").lower()

        if item_choice == "done":
            # Calculate tip and tax
            tip = food_total * Decimal(0.18)
            tax = food_total * Decimal(0.07)
            total = food_total + tip + tax

            # Receipt
            print("\nReceipt:")
            print(f"Food Total: ${food_total:.2f}")
            print(f"18% Tip:    ${tip:.2f}")
            print(f"7% Tax:     ${tax:.2f}")
            print(f"Total Due:  ${total:.2f}")
            break

        elif item_choice in menu:
            food_total += menu[item_choice]
            print(f"Added {item_choice.title()} - ${menu[item_choice]:.2f}")
        else:
            print("Item not on the menu. Try again.")

elif choice == "2":
    # Calculate tip and tax
    food_total = Decimal(input("Enter the total food charge: $"))
    tip = food_total * Decimal(0.18)
    tax = food_total * Decimal(0.07)
    total = food_total + tip + tax

    # Receipt
    print("\nReceipt:")
    print(f"Food Total: ${food_total:.2f}")
    print(f"18% Tip:    ${tip:.2f}")
    print(f"7% Tax:     ${tax:.2f}")
    print(f"Total Due:  ${total:.2f}")