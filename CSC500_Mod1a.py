from decimal import Decimal

# Get user input
num1 = Decimal(input("Please enter first number: "))
num2 = Decimal(input("Please enter second number: "))

# Calculations
add = num1 + num2
subtract = num1 - num2

# Results
print("Addition result:", add)
print("Subtraction result:", subtract)