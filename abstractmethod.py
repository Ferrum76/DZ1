from abc import ABC, abstractmethod

class ObjectCreationMixin:
    def __repr__(self):
        attributes = ', '.join(f"{attr}={getattr(self, attr)}" for attr in self.__dict__)
        return f"{self.__class__.__name__}({attributes})"

class AbstractProduct(ABC):

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_additional_info(self):
        pass

