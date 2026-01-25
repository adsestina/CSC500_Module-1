# Item cost, description and quantity
class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def total_cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        print(
            f"{self.item_name} "
            f"{self.item_quantity} @ ${self.item_price} = ${self.total_cost()}"
        )

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

# Shopping Cart
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def find_item_by_name(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                return item
        return None

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        item = self.find_item_by_name(item_name)
        if not item:
            print("Item not found in cart. Nothing removed.")
            return
        self.cart_items.remove(item)

    def modify_item(self, item_to_purchase):
        item = self.find_item_by_name(item_to_purchase.item_name)
        if not item:
            print("Item not found in cart. Nothing modified.")
            return

        if item_to_purchase.item_description != "none":
            item.item_description = item_to_purchase.item_description
        if item_to_purchase.item_price != 0:
            item.item_price = item_to_purchase.item_price
        if item_to_purchase.item_quantity != 0:
            item.item_quantity = item_to_purchase.item_quantity

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.total_cost() for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")

        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return

        print(f"Number of Items: {self.get_num_items_in_cart()}")

        for item in self.cart_items:
            item.print_item_cost()

        print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")

        for item in self.cart_items:
            item.print_item_description()

# Action handlers
def handle_add_item(cart):
    print("ADD ITEM TO CART")
    name = input("Enter the item name:\n")
    description = input("Enter the item description:\n")
    price = int(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))

    item = ItemToPurchase(name, description, price, quantity)
    cart.add_item(item)
    print()


def handle_remove_item(cart):
    print("REMOVE ITEM FROM CART")
    name = input("Enter name of item to remove:\n")
    cart.remove_item(name)
    print()


def handle_change_quantity(cart):
    print("CHANGE ITEM QUANTITY")
    name = input("Enter the item name:\n")
    quantity = int(input("Enter the new quantity:\n"))

    item = ItemToPurchase(item_name=name, item_quantity=quantity)
    cart.modify_item(item)
    print()


def print_menu(cart):
    # using lambda function
    actions = {
        "a": lambda: handle_add_item(cart),
        "r": lambda: handle_remove_item(cart),
        "c": lambda: handle_change_quantity(cart),
        "o": lambda: (
            print("\nOUTPUT SHOPPING CART"),
            cart.print_total(),
            print(),
        ),
        "i": lambda: (
            print("\nOUTPUT ITEMS' DESCRIPTIONS"),
            cart.print_descriptions(),
            print(),
        ),
    }
# Only acceptable selections
    valid_choices = {"a", "r", "c", "i", "o", "q"}

# Main Menu loop
    while True:
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        choice = input("Choose an option:\n")

        if choice not in valid_choices:
            print("Invalid selection. Please try again.\n")
            continue

        if choice == "q":
            break

        action = actions.get(choice)
        if action:
            action()


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()

