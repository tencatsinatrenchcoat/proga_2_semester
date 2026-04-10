# Lab02

## Предметная область

Интернет-магазин

Класс Customer

Коллекция Clientabse объектов Customer


## Использование

1. Базовые действия
```
создадим 4 клиентов, третий забанен

создадим коллекцию

добавим пользователей

[Client('Ada Lovelace', 'ada@mail.uk', 100000, 100), Client('John Von Neumann', 'john@mail.usa', 20000, 250), Client('Apple Inc.', 'apple@mail.usa', 999999999, 0), Client('Samsung Inc.', 'samsung@mail.sk', 999956799, 0)]

удалим второго

получим

[Client('Ada Lovelace', 'ada@mail.uk', 100000, 100), Client('Apple Inc.', 'apple@mail.usa', 999999999, 0), Client('Samsung Inc.', 'samsung@mail.sk', 999956799, 0)]

```

2. Поиск, итерация, длина
```
количество клиентов
3

проверка iter
Профиль клиента. 
Имя: Ada Lovelace 
Email: ada@mail.uk 
Баланс: 100000 $ 
Бонусные баллы: 100 

Профиль клиента. 
Имя: Apple Inc. 
Email: apple@mail.usa 
Баланс: 999999999 $ 
Бонусные баллы: 0 

Профиль клиента. 
Имя: Samsung Inc. 
Email: samsung@mail.sk 
Баланс: 999956799 $ 
Бонусные баллы: 0 
```

3. Фильтрация, работа с индексами, поиск
```
найдем пользователя Ada lovelace по email

Профиль клиента. 
Имя: Ada Lovelace 
Email: ada@mail.uk 
Баланс: 100000 $ 
Бонусные баллы: 100 

попробуем добавить дубликат
НЕЛЬЗЯ ДОБАВЛЯТЬ ДУБЛИКАТЫ

клиент по индексу 0: Ada Lovelace
последний клиент: Samsung Inc.

попытка найти клиента с несцщетсвующим индексом
ТАКОГО ИНДЕКСА НЕТ

сортировка
 отсортированные клиенты: [Client('Ada Lovelace', 'ada@mail.uk', 100000, 100), Client('Apple Inc.', 'apple@mail.usa', 999999999, 0), Client('Samsung Inc.', 'samsung@mail.sk', 999956799, 0)]

фильтр по бану
коллекция забаненых: [Client('Apple Inc.', 'apple@mail.usa', 999999999, 0)]
```