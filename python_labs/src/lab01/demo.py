from model import Customer

def main():
    print("Название магазина:", Customer.shop_name)
    print("======")
    print("неправильное создание с неверным типом в bonus")
    try:
        person1 = Customer("John Von Neumann", "john@google.com", 10000, "three")
        print(person1)
    except TypeError as e:
        print("текст ошибки", e)

    print("======")

    print("корректное создание")

    person2 = Customer("Ada Lovelace", "ada@yahoo.com", 2000000, 350 )
    print(person2)
    
    print("======")

    person1corr = Customer("John Von Neumann", "john@google.com", 10000, 3)

    print("cравнение 2 клиентов с разным email")
    print(Customer.__eq__(person2, person1corr))

    print("======")

    print("проверка ограничения на баланс")
    try:
        person2.balance_increase(-200000)
    except ValueError as e:
        print(e)

    print("======")

    print(f"бонусы до:{person2._bonus_points}")
    person2.bonus_points = 100
    print(f"бонусы после изменения через setter: {person2._bonus_points}")

    print("======")
    print("доступ через класс")
    print(f"название магазина: {Customer.shop_name}")
    print("доступ через экземпляр")
    print(f"имя клиента {person2.name}")
    print("======")
    print("демонстрация логических состояний")
    print(f"is account banned: {person2._banned}")
    person2.ban()
    print(f"change of state: {person2._banned}")
    print("attempt to buy")
    person2.make_purchase(2000, 10)
    print("attempt to buy from working account")
    print("before")
    print(person1corr)
    person1corr.make_purchase(300, 1)
    print("bought item for 300, used 1 bonus\n")
    print("after\n")

    print(person1corr)
    print("======") 



if __name__ == "__main__":
    main()