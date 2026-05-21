from collection import Clientbase
from models import HumanCustomer, CorporateCustomer
from strategies import by_name, by_email_and_name, by_wallet_balance, filter_by_balance, filter_is_corporate

cc1 = CorporateCustomer("x5 group", "x5@mail.ru", 400000, 1000000, 15)
cc2 = CorporateCustomer("Samsung Inc.", "samsung@mail.sk", 999956799, 500000, 660)
cc3 = CorporateCustomer("Apple Inc.", "apple@mail.usa", 999999999, 100000000, 2150)
hc1 = HumanCustomer("Ada Lovelace", "ada@mail.uk", 100000, 100, "+70000001234", "самовывоз")
hc2 = HumanCustomer("John Von Neumann", "john@mail.usa", 20000, 250, "+71111113456", "курьер")

items = [cc1, cc2, cc3, hc1, hc2]

c = Clientbase(items)

print("коллекция")
print(c.get_all())

print("сортировка по имени")

print(c.sort(by_name))

print("сортировка по балансу")

print(c.sort(by_wallet_balance))

print("сортировка по имени и email")

print(c.sort(by_email_and_name))

print("фильтрация по количеству денег в кошельке больше указанной суммы")

print(c.filter(filter_by_balance(2000000)))

print("фильтрация корпоративный клиент или нет")

print(c.filter(filter_is_corporate))