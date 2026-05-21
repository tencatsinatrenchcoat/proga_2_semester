# Лабораторная №5
Передача функций как аргументов
lambda, map, filter
## Реализовано
# sort
by_name
by_email_and_name
by_wallet_balance

# filter
filter_by_balance - выдает список клиентов, у которых баланс больше заданного 
filter_is_corporate

## Работа функций

```
коллекция
[Client('x5 group', 'x5@mail.ru', 400000, 0), Client('Samsung Inc.', 'samsung@mail.sk', 999956799, 0), Client('Apple Inc.', 'apple@mail.usa', 999999999, 0), Client('Ada Lovelace', 'ada@mail.uk', 100000, 100), Client('John Von Neumann', 'john@mail.usa', 20000, 250)]
```
```
сортировка по имени

[Client('Ada Lovelace', 'ada@mail.uk', 100000, 100), Client('Apple Inc.', 'apple@mail.usa', 999999999, 0), Client('John Von Neumann', 'john@mail.usa', 20000, 250), Client('Samsung Inc.', 'samsung@mail.sk', 999956799, 0), Client('x5 group', 'x5@mail.ru', 400000, 0)]
```
```
сортировка по балансу
[Client('John Von Neumann', 'john@mail.usa', 20000, 250), Client('Ada Lovelace', 'ada@mail.uk', 100000, 100), Client('x5 group', 'x5@mail.ru', 400000, 0), Client('Samsung Inc.', 'samsung@mail.sk', 999956799, 0), Client('Apple Inc.', 'apple@mail.usa', 999999999, 0)]
```
```
сортировка по имени и email
[Client('Ada Lovelace', 'ada@mail.uk', 100000, 100), Client('Apple Inc.', 'apple@mail.usa', 999999999, 0), Client('John Von Neumann', 'john@mail.usa', 20000, 250), Client('Samsung Inc.', 'samsung@mail.sk', 999956799, 0), Client('x5 group', 'x5@mail.ru', 400000, 0)]
```
```
фильтрация по количеству денег в кошельке больше указанной суммы (2000000)
[Client('Samsung Inc.', 'samsung@mail.sk', 999956799, 0), Client('Apple Inc.', 'apple@mail.usa', 999999999, 0)]
```
```
фильтрация корпоративный клиент или нет
[Client('x5 group', 'x5@mail.ru', 400000, 0), Client('Samsung Inc.', 'samsung@mail.sk', 999956799, 0), Client('Apple Inc.', 'apple@mail.usa', 999999999, 0)]
```

## Вывод
Реализованы функции фильтрации и сортировки с помощью lambda функций, изучен паттерн стратегия и передача функций  как аргументов