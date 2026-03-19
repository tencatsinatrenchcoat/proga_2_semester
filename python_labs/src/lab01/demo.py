from model import Customer

def main():

    customer1 = Customer("Ada Lovelace", "ada@mail.uk", 10000, 250)
    print("=== обычная покупка ===")
    print(customer1)
    print("баланс +500 ")
    customer1.balance_increase(500)
    print(f"новый баланс: {customer1.wallet_balance} $")
    print("\n покупка на 500 без использования бонусов")
    customer1.make_purchase(500, 0)
    print(customer1)


    print("\n=== покупка с бонусами ===")
    print("совершаем покупку на 400, используя 100 бонусов")
    customer1.make_purchase(400, 100)
    print(customer1)


    customer1.ban()
    print("\n=== заблокированный аккаунт ===")
    print("заблокируем клиента")
    print("пытаемся пополнить баланс")
    customer1.balance_increase(200)
    print("пытаемся совершить покупку")
    customer1.make_purchase(100, 0)
    print("\n разблокируем клиента")
    customer1.unban()
    print("повторяем покупку на 100 $")
    customer1.make_purchase(100, 0)
    print(customer1)

    print("\n=== dunder methods ===")
    print("__str__")
    print(customer1)
    print("__repr__")
    print(customer1.__repr__)
    print("__eq__")
    print("cравним двух клиентов")
    customer2 = Customer("John Von Neumann", "john@mail.us", 38000, 387)
    print(customer1 == customer2)



if __name__ == "__main__":
    main()