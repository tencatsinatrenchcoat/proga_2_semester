from model import Customer
from collection import Clientbase
# создание нескольких объектов
# добавление их в коллекцию
# вывод всех элементов
# удаление элемента
# повторный вывод коллекции



# В demo.py показать:

#     поиск элемента
#     использование len()
#     использование for
#     работу ограничения на дубликаты

# показать индексацию
# показать сортировку
# показать фильтрацию
# показать несколько сценариев работы коллекции

print()
c1 = Customer("Ada Lovelace", "ada@mail.uk", 100000, 100)
c2 = Customer("John Von Neumann", "john@mail.usa", 20000, 250)
c3 = Customer("Apple Inc.", "apple@mail.usa", 999999999, 0)
c3.ban()

print()
userbase = Clientbase()

print()
userbase.add(c1)
userbase.add(c2)
userbase.add(c3)

print()
userbase.get_all()

print()
userbase.remove(c2)

print()
userbase.get_all()

print()
userbase.find_by_email("ada@mail.uk")

print()
len(userbase)

# for item in collection ????? from iter 

c4 = Customer("ANot da Lovelace", "ada@mail.uk", 100000, 100)
userbase.add(c4) # todo make error not like that