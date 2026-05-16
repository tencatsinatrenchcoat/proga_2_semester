from collection import Clientbase
from models import CorporateCustomer, HumanCustomer


def print_all_printable(items: list[Printable]):
    for item in items:
        if not isinstance(item, Printable):
            raise TypeError("объект не реализует интерфейс")
        print(item.to_string())

def print_all_delivery_avaliable(items: list[Delivery_avaliable]):
    for item in items:
        if not isinstance(item, Delivery_avaliable):
            raise TypeError("объект не реализует интерфейс")
        print(item.calculate_delivery_price())

cc1 = CorporateCustomer("x5 group", "x5@mail.ru", 4, 100000, 15)
cc2 = CorporateCustomer("Samsung Inc.", "samsung@mail.sk", 999956799, 500000, 660)
cc3 = CorporateCustomer("Apple Inc.", "apple@mail.usa", 999999999, 100000000, 2150)

hc1 = HumanCustomer("Ada Lovelace", "ada@mail.uk", 100000, 100, "+70000000000", "самовывоз")
hc2 = HumanCustomer("John Von Neumann", "john@mail.usa", 20000, 250, "+71111111111", "курьер")
hc3 = HumanCustomer("Steve Jobs", "steve@mail.usa", 35000, 666, "+72222222222", "пункт выдачи")

items = [cc1, cc2, cc3]
cl = Clientbase(items)

print(cl.sort_by_delivery_price())