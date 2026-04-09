from validators import _validate_bonus, _validate_email, _validate_pos_values, _validate_wallet, _validate_name
class Customer:
    shop_name = "PC Parts Shop"
    def __init__(self, name: str, email: str, wallet_balance: float, bonus_points: int):
        _validate_name(name)
        _validate_email(email)
        _validate_wallet(wallet_balance)
        _validate_bonus(bonus_points)
        self._name = name
        self._email = email
        self._wallet_balance = wallet_balance
        self._bonus_points = bonus_points

        self._banned = False #state

#properties

    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @property
    def wallet_balance(self):
        return self._wallet_balance
    
    @property
    def bonus_points(self):
        return self._bonus_points

    @property
    def banned(self):
        return self._banned

#setters

    @name.setter
    def name(self, value):
        _validate_name(value)
        self._name = value

    @email.setter
    def email(self, value):
        _validate_email(value)
        self._email = value

    @wallet_balance.setter
    def wallet_balance(self, value):
        _validate_wallet(value)
        self._wallet_balance = value

    @bonus_points.setter
    def bonus_points(self, value):
        _validate_bonus(value)
        self._bonus_points = value

#dunder methods

    def __str__(self):
        return (f"Профиль клиента. \n"
            f"Имя: {self._name} \n"
            f"Email: {self._email} \n"
            f"Баланс: {self._wallet_balance} $ \n"
            f"Бонусные баллы: {self._bonus_points} \n")

    def __repr__(self):
        return (
            f"Client('{self._name}', "
            f"'{self._email}', "
            f"{self._wallet_balance}, "
            f"{self._bonus_points})"
        )

    def __eq__(self, other):
        return self._email == other._email

#business methods

    def balance_increase(self, amount):
        if not self._banned:
            _validate_pos_values(amount)
            self._wallet_balance += amount
        else:
            print("баланс данного аккаунта нельзя пополнить")

        _validate_pos_values(amount)
        self._wallet_balance += amount

    def make_purchase(self, price, use_points):
        if self._banned:
            print("с данного аккаунта нельзя совершать покупки")
        else:
            _validate_pos_values(price)
            _validate_pos_values(use_points)

            if self._wallet_balance + use_points >= price and self._bonus_points >= use_points :
                self._wallet_balance -= price - use_points
                self._bonus_points -= use_points
                self._bonus_points += price * 0.05 
            else:
                print("недостаточно средств")

#state change

    def ban(self):
        self._banned = True
    
    def unban(self):
        self._banned = False