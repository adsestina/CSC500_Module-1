from decimal import Decimal

# Get user input
num1 = Decimal(input("Please enter first number: "))
num2 = Decimal(input("Please enter second number: "))

# Calculations
multiply = num1 * num2

# Check for division by zero
if num2 != 0:
    divide = num1 / num2
else:
    divide = "Undefined (cannot divide by zero)"

# Results
print("Multiplication result:", multiply)
print("Division result:", divide)