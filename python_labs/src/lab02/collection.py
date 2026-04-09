from model import Customer

class Clientbase:
#3  
    def __init__(self, items = None): 
        self._items = [] 
        if items is not None:
            for item in items:
                self.add(item)
    
    def add(self, item):
        if not isinstance(item, Customer):
            raise TypeError("! нельзя добавить объект, не являющийся клиентом")
        for customer in self._items:
            if customer.email == item.email:
                raise ValueError("! нельзя добавить клиента с тем же email")
        self._items.append(item)

    def remove(self, item):
        if item not in self._items:
            raise ValueError("! такого клиента нет")
        self._items.remove(item)

    def get_all(self):
        return self._items.copy()

#4
    def find_by_email(self, email):
        for item in self._items:
            if item.email == email:
                return item
        return "! не найдено"
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)

#5 
    def __getitem__(self, index):
        try:
            return self._items[index]
        except IndexError:
            raise IndexError("! такого индекса нет")

    def remove_at(self, index):
        try:
            del self._items[index]
        except IndexError:
            raise IndexError("! такого индекса нет")

    def sort_by_email(self, email):
        self._items.sort(key = lambda customer: customer_email)
        
    def get_banned(self):
        banned_collection = []
        for customer in self._items:
            if customer._banned is True:
                banned_collection.append(customer)
        return banned_collection

