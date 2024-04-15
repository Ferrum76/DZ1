from abstractmethod import AbstractProduct, ObjectCreationMixin


class Category:
    total_categories = 0
    all_unique_products = set()  # Global tracking of unique products

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        # Ensures unique products at initialization
        self.__products = list(set(products))
        Category.total_categories += 1
        Category.all_unique_products.update(self.__products)

    def add_product(self, product):
        if isinstance(product, Product):
            if product not in self.__products:
                self.__products.append(product)
                Category.all_unique_products.add(product)
        else:
            raise AttributeError

    def remove_product(self, product):
        if product in self.__products:
            self.__products.remove(product)

    def get_products(self):
        return self.__products

    def get_products_info(self):
        products_info = []
        for product in self.__products:
            info = f"{product.name}, {
                product.price} руб. Остаток: {product.quantity} шт."
            products_info.append(info)
        return products_info

    @classmethod
    def get_total_unique_products(cls):
        return len(cls.all_unique_products)

    def __str__(self):
        total_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_products} шт."


class Product(AbstractProduct, ObjectCreationMixin):
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
        if isinstance(other, Product):
            return self.price*self.quantity + other.price*other.quantity
        return AttributeError

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product, ObjectCreationMixin):
    def __init__(self, name, description, price, quantity, performance, model, memory_capacity, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity
        self.color = color


class LawnGrass(Product, ObjectCreationMixin):
    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color