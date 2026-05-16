
def print_all(items: list[Printable]):
    for item in items:
        print(item.to_string())

def print_all(items: list[Deliverable]):
    for item in items:
        print(item.delivery_price_calculator())


print("Printable:", isinstance(obj, Printable))
print("Deliverable:", isinstance(obj, Deliverable))


