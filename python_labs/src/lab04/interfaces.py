from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def to_string(self):
        pass

class Deliverable(ABC):
    @abstractmethod
    def delivery_price_calculator(self):
        pass

