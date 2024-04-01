from abc import ABC, abstractmethod

class ObjectCreationMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ', '.join(f"{attr}={getattr(self, attr)}" for attr in self.__dict__)
        return f"{class_name}({attributes})"

class AbstractProduct(ABC):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректная")
        else:
            self.__price = new_price

    @abstractmethod
    def get_additional_info(self):
        pass

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

