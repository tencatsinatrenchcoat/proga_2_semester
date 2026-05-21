from collection import Clientbase
from models import CorporateCustomer, HumanCustomer
from interfaces import Printable, Delivery_avaliable

def print_all_printable(items: list[Printable]):
    for item in items:
        if not isinstance(item, Printable):
            raise TypeError("объект не реализует интерфейс")
        print(item.to_string())

def print_all_delivery_avaliable(items: list[Delivery_avaliable]):
    for item in items:
        if not isinstance(item, Delivery_avaliable):
            raise TypeError("объект не реализует интерфейс")
        print(item._name, item.calculate_delivery_price())  # type: ignore


cc = CorporateCustomer("Samsung Inc.", "samsung@mail.sk", 999956799, 500000, 156)


hc = HumanCustomer("Ada Lovelace", "ada@mail.uk", 100000, 100, "+70000000000", "самовывоз")



items = [ cc, hc]

# единый список объектов разных типов
# работа через интерфейсы
# фильтрация коллекции по интерфейсу
# минимум 3 сценария
def sc1():
    cl = Clientbase(items)
    print(cl.get_all())

    print_all_printable(items)

    print_all_delivery_avaliable(items)

def sc2():

    print("Printable:", isinstance(hc, Printable))
    print("Payable:", isinstance(hc, Delivery_avaliable))

def sc3(): 
    cl = Clientbase(items)
    print(cl.sort_by_delivery_price())
    pass


sc1()
sc2()
sc3()
