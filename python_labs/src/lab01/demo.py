from model import Customer

def main():
    print("Название магазина:", Customer.shop_name)

    person2 = Customer("Ada Lovelace", "ada@yahoo.com", 2000000, 350 )
    print(person2)


    person1 = Customer("John Von Neumann", "john@google.com", 10000, "three")
    print(person1)


if __name__ == "__main__":
    main()