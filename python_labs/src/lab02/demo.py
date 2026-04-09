from model import Customer
from collection import Clientbase

print("создадим трех клиентов, третий забанен")
c1 = Customer("Ada Lovelace", "ada@mail.uk", 100000, 100)
c2 = Customer("John Von Neumann", "john@mail.usa", 20000, 250)
c3 = Customer("Apple Inc.", "apple@mail.usa", 999999999, 0)
c3.ban()

print("создадим коллекцию")
userbase = Clientbase()

print("добавим пользователей")
userbase.add(c1)
userbase.add(c2)
userbase.add(c3)

print(userbase.get_all())

print("удалим второго")
userbase.remove(c2)

print("получим")
print(userbase.get_all())

print("найдем пользователя по email")
print(userbase.find_by_email("ada@mail.uk"))

print("количество клиентов")
print(len(userbase))

print("проверка iter")
for item in userbase:
    print(item)

print("попробуем добавить дубликат")
c4 = Customer("ANot da Lovelace", "ada@mail.uk", 100000, 100)
try: 
    userbase.add(c4) 
except ValueError:
    print("НЕЛЬЗЯ ДОБАВЛЯТЬ ДУБЛИКАТЫ")

print(f"клиент по индексу 0: {userbase[0].name}")
print(f"последний клиент: {userbase[-1].name}")

print("попытка найти клиента с несцщетсвующим индексом")
try:
    userbase[100].name
except IndexError:
    print("ТАКОГО ИНДЕКСА НЕТ")

print("сортировка")
sorted_clients = userbase.sort_by_email()
print(f" отсортированные клиенты: {sorted_clients}")

print("фильтр по бану")
banned_clients = userbase.get_banned()
print(f"коллекция забаненых: {banned_clients.get_all()}")