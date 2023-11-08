class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}₴"

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def show_products(self):
        print(f"Products in {self.name}:")
        for product in self.products:
            print(product)

product1 = Product("Crackers", 23)
product2 = Product("PopCorn", 45)
product3 = Product("Chocolate", 15)
product4 = Product("Bubble gum", 20)

store = Store("АТБ")

store.add_product(product1)
store.add_product(product2)
store.add_product(product3)
store.add_product(product4)

store.show_products()

store.remove_product(product3)

store.show_products()