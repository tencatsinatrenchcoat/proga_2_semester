from models import CorporateCustomer, HumanCustomer
from collection import *

cc1 = CorporateCustomer("x5 group", "x5@mail.ru", 400000, 1000000, 15)
cc2 = CorporateCustomer("Samsung Inc.", "samsung@mail.sk", 999956799, 500000, 660)
cc3 = CorporateCustomer("Apple Inc.", "apple@mail.usa", 999999999, 100000000, 2150)

hc1 = HumanCustomer("Ada Lovelace", "ada@mail.uk", 100000, 100, "+70000000000", "самовывоз")
hc2 = HumanCustomer("John Von Neumann", "john@mail.usa", 20000, 250, "+71111111111", "курьер")
hc3 = HumanCustomer("Steve Jobs", "steve@mail.usa", 35000, 666, "+72222222222", "пункт выдачи")


def scenario1():

    print(cc1.__str__())

    print(cc1.display())

    cc1.make_purchase(35000)

    print(cc1.display())

    pass

def scenario2():

    print(hc3.__str__())

    print(hc3.display())

    hc3.make_purchase(200, 30)

    print(hc3.display())

    print(hc3.pickup_code_generator())
    pass

def scenario3():

    items = [cc1, cc2, cc3, hc1, hc2, hc3]
    cl = Clientbase(items)

    print(cl.get_all())

    print(cl.get_corpo_customer())
    
    print(cl.get_human_customer())
    pass

scenario1()
scenario2()
scenario3()