from base import Customer
from validators import _validate_pos_values, _validate_delivery, _validate_phone

class CorporateCustomer(Customer):
    def __init__(self, name, email, wallet_balance, order_limit: int, warehouse_distance: (int, float), bonus_points = 0, banned = False):
        _validate_pos_values(order_limit)
        _validate_pos_values(warehouse_distance)
        super().__init__(name, email, wallet_balance, bonus_points)
        self._order_limit = order_limit
        self._warehouse_distance = warehouse_distance

    @property
    def order_limit(self):
        return self._order_limit

    @property
    def warehouse_distance(self):
        return self._warehouse_distance

    @order_limit.setter
    def order_limit(self, value):
        _validate_pos_values(value)
        self._order_limit = value

    @warehouse_distance.setter
    def warehouse_distance(self, value):
        _validate_pos_values(value)
        self._warehouse_distance = value

    def ability_to_order(desired_purchase):
        return desired_purchase <= self._order_limit

    def __str__():
        return (f"Профиль клиента. \n"
            f"Имя: {self._name} \n"
            f"Email: {self._email} \n"
            f"Баланс: {self._wallet_balance} $ \n"
            f"Бонусные баллы: {self._bonus_points} \n"
            f"Лимит на сумму заказа: {self._item_order_limit} $ \n"
            f"Расстояние от магазина до склада: {self._warehouse_distance} км")

    def delivery_price_calculator(self): # 4
        if self._warehouse_distance <= 200:
            price = self._warehouse_distance * 1.5 * 75
        else: 
            price = self._warehouse_distance * 1.5 * 150
        return f"Стоимость доставки {price} $"


    def make_purchase(self, price):
        if self._banned:
            print("с данного аккаунта нельзя совершать покупки")
        else:
            _validate_pos_values(price)
            _validate_pos_values(use_points)

            if self._wallet_balance >= price and self._order_limit >= price:
                self._wallet_balance -= price + delivery_price_calculator(self)
            else:
                print("недостаточно средств или вы не можете сделать заказ на такую сумму")

    def display(self):
        delivery = self._delivery_price_calculator()
        return f"Ваш баланс {self._wallet_balance}, вы можете сделать заказ на сумму {self._order_limit}, доставка будет стоить {delivery}"


class HumanCustomer(Customer):
    def __init__(self, name, email, wallet_balance, bonus_points, phone_number: str, delivery_method: str, banned = False):
        _validate_phone(phone_number)
        _validate_delivery(delivery_method)
        super().__init__(name, email, wallet_balance, bonus_points)
        self._phone_number = phone_number
        self._delivery_method = delivery_method

    @property
    def delivery_method(self):
        return self._delivery_method

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        _validate_phone(value)
        self._phone_number = value

    @delivery_method.setter
    def delivery_method(self, value):
        _validate_delivery(value)
        self._delivery_method = value

    def __str__():
        return (f"Профиль клиента. \n"
            f"Имя: {self._name} \n"
            f"Email: {self._email} \n"
            f"Баланс: {self._wallet_balance} $ \n"
            f"Бонусные баллы: {self._bonus_points} \n"
            f"НОмер телефона: {self._phone_number}\n"
            f"Способ доставки: {self._delivery_method}")

    def pickup_code_generator(phone_number):
        return phone_number[:4]
            
    def delivery_price_calculator(self): #4
        if self._delivery_method == "самовывоз":
            price = 0
        if self._delivery_method == "пункт выдачи":
            price = 10
        if self._delivery_method == "курьер":
            price = 20
        return f"Ваша стоимость доставки {price} $"

    def make_purchase(self, price, use_points):
        if self._banned:
            print("с данного аккаунта нельзя совершать покупки")
        else:
            _validate_pos_values(price)
            _validate_pos_values(use_points)

            if self._wallet_balance + use_points >= price and self._bonus_points >= use_points :
                self._wallet_balance -= price - use_points + delivery_price_calculator(self)
                self._bonus_points -= use_points
                self._bonus_points += price * 0.05 
            else:
                print("недостаточно средств")

    def display(self):
        delivery = self._delivery_price_calculator()
        return (f"Ваш баланс {self._wallet_balance} $, ваши баллы {self._bonus_points}, доставка бдует стоить {delivery} $")