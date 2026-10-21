# 1. The Base Class: Product
# Create a base class called Product with the following requirements:
# Encapsulation: It should have private or protected attributes for product_id, name, price, and stock_quantity.
# Getters and Setters: Provide appropriate methods (or properties) to securely access and update these attributes (e.g., updating stock shouldn't allow negative numbers).


# Methods:
# update_stock(amount): Adds or subtracts from the current stock quantity.
# get_details(): Returns a string summary of the product.
# calculate_discount_price(): A base method that returns the standard price (can be overridden by subclasses).


# 2. Subclasses (Inheritance & Polymorphism)
# Create at least two specialized product subclasses that inherit from Product:
# Electronics:
# Add a unique attribute like warranty_months (integer).
# Override calculate_discount_price() to apply a seasonal discount (e.g., 10% off if the price is above a certain threshold, or a flat percentage).
# Clothing:
# Add attributes like size (string) and material (string).
# Override calculate_discount_price() to apply a clearance discount (e.g., 20% off).

# 3. The Management Class: Inventory (Composition)
# Create an Inventory class that manages a collection of products:
# It should contain a list or dictionary to store multiple Product objects.

# Methods:
# add_product(product): Adds a product to the inventory.
# remove_product(product_id): Removes a product by its ID.
# get_total_inventory_value(): Calculates and returns the total financial value of all items currently in stock (price × stock_quantity for all products).
# list_products(): Displays details for all items in the inventory.

class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id =product_id
        self.name = name
        self._stock_quantity = stock_quantity
        self.__price = price

#Product summary
    def get_details(self):
        return f" Product summary: {self.product_id}, {self.name} has stock of {self._stock_quantity}"

#Get item price
    def get_item_price(self):
        return self.__price

#Update stock amounts
    def update_stock(self, amount):
        if self._stock_quantity < 0:
            print(f"Current stock is low!")
        else:
            self._stock_quantity += amount
            print(f"Stock quantity successfully updated.")


class Electronics(Product):
    def __init__(self, product_id, name, price, stock_quantity, warranty):
        super().__init__(product_id, name, price, stock_quantity)
        self.warranty = warranty

#Discount for all electronics
    def calculate_discount_price(self, discount):
        self.discount = (1 - discount)
        return self.get_item_price() * self.discount
    
class Clothing(Product):
    def __init__(self, product_id, name, price, stock_quantity, size, material):
        super().__init__(product_id, name, price, stock_quantity)
        self.size = size
        self.material =material

#20% clearence discount on clothing
    def calculate_discount_price(self, discount):
        self.discount = discount
        return self.get_item_price() * (1 - discount)



# add_product(product): Adds a product to the inventory.

# remove_product(product_id): Removes a product by its ID.

# get_total_inventory_value(): Calculates and returns the total financial value of all items currently in stock (price × stock_quantity for all products).

# list_products(): Displays details for all items in the inventory

class Inventory:
    def __init__(self):
        self.items = []

#Add products to inventory
    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} successfully added to inventory")

#Remove product by ID
    def remove_product(self, id):
        self.items.remove(id)
        print(f"Product with {id.name} successfully removed")

    def list_products(self):
        for product in self.items:
            print(product.get_details())