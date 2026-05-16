
def print_all_printable(items: list[Printable]):
    for item in items:
        print(item.to_string())

def print_all_deliverable(items: list[Deliverable]):
    for item in items:
        print(item.calculate_delivery_price())

