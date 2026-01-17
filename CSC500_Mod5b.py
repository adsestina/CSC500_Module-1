# CSU bookstore points system
points_dict = {
    0: 0,
    2: 5,
    4: 15,
    6: 30,
    8: 60
}

books_purchased = int(input("Enter the number of books purchased this month: "))

# find the key less than or equal to books_purchased
eligible_points = [k for k in points_dict if k <= books_purchased]

# Get the next lowest amount of points if not equal
points = points_dict[max(eligible_points)] if eligible_points else 0

print(f"You earned {points} points this month.")