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
        if isinstance(product, Product):
            if product not in self.__products:
                self.__products.append(product)
                Category.all_unique_products.add(product)
        else :
            raise AttributeError

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
        total_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_products} шт."



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
        if isinstance(other, Product):
            return self.price*self.quantity + other.price*other.quantity
        return AttributeError

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, performance, model, memory_capacity, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color


# Создаем продукты
product1 = Product("Тетрадь", "Тетрадь в клетку", 50, 20)
product2 = Smartphone("Смартфон", "Смартфон с хорошей камерой", 500, 10, "Высокая", "iPhone 13", "128 ГБ", "черный")
product3 = LawnGrass("Трава газонная", "Трава для газонов", 100, 5, "Россия", "14 дней", "зеленый")

# Проверяем вывод информации о продуктах
print(product1)
print(product2)
print(product3)

# Проверяем сложение товаров разных классов
try:
    result_product = product1 + product2
except TypeError as e:
    print("Ошибка:", e)

# Проверяем сложение товаров одного класса
result_product = product2 + product2
print(result_product)

# Создаем категорию
category = Category("Товары", "Все товары")

# Попытка добавить объекты других классов в категорию
try:
    category.add_product("Просто строка")
except TypeError as e:
    print("Ошибка:", e)

try:
    category.add_product(12345)
except TypeError as e:
    print("Ошибка:", e)

# Добавляем продукты в категорию
category.add_product(product1)
category.add_product(product2)
category.add_product(product3)

# Проверяем, что все продукты успешно добавлены
print("Продукты в категории:")
for product in category.get_products():
    print(product)