class Category:
    total_categories = 0
    all_unique_products = set()  # Global tracking of unique products

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = list(set(products))  # Ensures unique products at initialization
        Category.total_categories += 1
        Category.all_unique_products.update(self.__products)


    def add_product(self, product):
        if product not in self.__products:
            self.__products.append(product)
            Category.all_unique_products.add(product)

    def remove_product(self, product):
        if product in self.__products:
            self.__products.remove(product)
    
    def get_products(self):
        return self.__products

    def get_products_info(self):
        products_info = []
        for product in self.__products:
            info = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            products_info.append(info)
        return products_info
    
    @classmethod
    def get_total_unique_products(cls):
        return len(cls.all_unique_products)

    def __str__(self):
        
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректная")
        else:
            self.__price = new_price

    def __add__(self, other):
        return self.price*self.quantity + other.price*other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
    