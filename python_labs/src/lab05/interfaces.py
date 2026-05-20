from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def to_string(self):
        pass

class Delivery_avaliable(ABC):
    @abstractmethod
    def calculate_delivery_price(self):
        pass

