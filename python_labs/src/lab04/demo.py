
def print_all_printable(items: list[Printable]):
    for item in items:
        if not isinstance(item, Printable):
            raise TypeError("объект не реализует интерфейс")
        print(item.to_string())

def print_all_delivery_avaliable(items: list[Delivery_avaliable]):
    for item in items:
        if not isinstance(item, Delivery_avaliable):
            raise TypeError("объект не реализует интерфейс")
        print(item.calculate_delivery_price())

