# Programmer: Arash
# Date: 11-18-2026
# Purpose: Track product details and inventory value.
# Instructor: Deodat Sharma


class Product:
    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def display_info(self):
        print(f"Product name: {self.name}")
        print(f"Product categhory: {self.category}")
        print(f"Product quantity: {self.quantity}")

    def inventory_value(self):
        return self.price * self.quantity

print("PLEASE ENTER INFO REGARD TO THE PRODUCTS")
print("-" * 50),
product1 = Product(
    
    input("Product 1 name: "),
    input("Product 1 category: "),
    int(input("Product 1 quantity: ")),
    float(input("Product 1 price: "))
)
print()
print("-" * 50)
print()
product2 = Product(
    input("Product 2 name: "),
    input("Product 2 category: "),
    int(input("Product 2 quantity: ")),
    float(input("Product 2 price: "))
)

print(f"Product 1: {product1.name}, {product1.category}, {product1.quantity}")
print(f"Product 2: {product2.name}, {product2.category}, {product2.quantity}")

