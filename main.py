class Category:
    total_categories = 0
    all_unique_products = set()  # Global tracking of unique products

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = list(set(products))  # Ensures unique products at initialization
        Category.total_categories += 1
        Category.all_unique_products.update(self.products)


    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
            Category.all_unique_products.add(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_unique_products():
        return len(Category.all_unique_products)

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
