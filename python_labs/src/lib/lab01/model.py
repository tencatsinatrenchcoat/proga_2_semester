class Customer:
    shop_name = "PC Parts Shop"
    def __init__(self, name: str, email: str, wallet_balance: float, bonus_points: int):
        self._name = name
        self._email = email
        self._wallet_balance = wallet_balance
        self._bonus_points = bonus_points

        self._not_banned = True #state

 #validators  

    def _validate_name(self, value):
        if not isinstance(value, str):
            raise TypeError("имя не строка")
        if len(value.strip()) < 2:
            raise ValueError("имя слишком короткое")

    def _validate_email(self, email):
        if not isinstance(value, str):
            raise TypeError("email не строка")
        if not "@" in value:
            raise ValueError("нет адреса домена")
        if len(value.strip()) < 2:
            raise ValueError("слишком короткий email")

    def _validate_wallet(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("сумма в кошельке не float/int")
        if value < 0:
            raise ValueError("баланс не может быть отрицательным")

    def _validate_bonus(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("количество бонусов не float/int")
        if not 100 > value > 0:
            raise ValueError("нельзя начислить более 100 бонусов за покупку")

    def _validate_pos_values(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("не float/int")
        if value < 0:
            raise ValueError("не может быть отрицаьельным значением")

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

#setters

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self.name = value

    @email.setter
    def email(self, value):
        self._validate_email(value)
        self.email = value

    @wallet_balance.setter
    def balance(self, value):
        self._validate_wallet(value)
        self._wallet_balance = value

    @bonus_points.setter
    def bonus_points(self, value):
        self._validate_bonus(value)
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
            f"{self._email}, "
            f"{self._wallet_balance}, "
            f"{self._bonus_points})"
        )

    def __eq__(self, other):
        return self._email == other._email

#business methods

    def balance_increase(self, amount, use_points = 0):
        if self._not_banned:
            self._validate_pos_values(amount)
            self._wallet_balance += amount
        else:
            print("баланс данного аккаунта нельзя пополнить")

        self._validate_pos_values(amount)
        self._wallet_balance += amount

    def make_purchase(self, price):
        if self._not_banned:
            self._validate_pos_values(price)
            self._validate_pos_values(use_points)
        else:
            print("с данного аккаунта нельзя совершать покупки")

        self._validate_pos_values(price)
        self._validate_pos_values(use_points)

        if self._wallet_balance + use_points >= price:
            self._wallet_balance -= price - use_points
            self._bonus_points -= use_points
            self._bonus_points += price * 0.05 
        else:
            print("недостаточно средств")

#state change

    def ban(self):
        if self._not_banned:
            self._not_banned = False
            print("аккаунт перманентно заблокирован")
        else:
            print("аккаунт уже заблокирован")
    
    