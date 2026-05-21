from collection import Clientbase
from models import HumanCustomer, CorporateCustomer

cc1 = CorporateCustomer("x5 group", "x5@mail.ru", 400000, 1000000, 15)
cc2 = CorporateCustomer("Samsung Inc.", "samsung@mail.sk", 999956799, 500000, 660)
cc3 = CorporateCustomer("Apple Inc.", "apple@mail.usa", 999999999, 100000000, 2150)
hc1 = HumanCustomer("Ada Lovelace", "ada@mail.uk", 100000, 100, "+70000001234", "самовывоз")
hc2 = HumanCustomer("John Von Neumann", "john@mail.usa", 20000, 250, "+71111113456", "курьер")