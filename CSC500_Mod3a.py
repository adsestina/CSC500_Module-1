#Importing for more precise monetary calculations
from decimal import Decimal

# Ask the user for the cost of the food
food_charge = Decimal(input("Enter the charge for the food: $"))

# Calculate tip and tax
tip = food_charge * Decimal(0.18)
tax = food_charge * Decimal(0.07)

# Calculate total
total = food_charge + tip + tax

# Results
print(f"\nFood Charge: ${food_charge:.2f}")
print(f"18% Tip:     ${tip:.2f}")
print(f"7% Tax:      ${tax:.2f}")
print(f"Total Price: ${total:.2f}")