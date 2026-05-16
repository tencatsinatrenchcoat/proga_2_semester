def _validate_name(name):
    if not isinstance(name, str) or len(name.strip()) <= 2:
        raise ValueError("имя должно быть непустое и больше 2 символов")

def _validate_email(value):
    if not isinstance(value, str):
        raise TypeError("email не строка")
    if not "@" in value:
        raise ValueError("нет адреса домена")
    if len(value.strip()) < 2:            
        raise ValueError("слишком короткий email")

def _validate_wallet(value):
    if not isinstance(value, (float, int)):
        raise TypeError("сумма в кошельке не float/int")
    if value < 0:
        raise ValueError("баланс не может быть отрицательным")

def _validate_bonus(value):
    if not isinstance(value, (float, int)):
        raise TypeError("количество бонусов не float/int")
    if not value >= 0:
        raise ValueError("бонусы не могут быть отрицательными")

def _validate_pos_values(value):
    if not isinstance(value, (float, int)):
        raise TypeError("не float/int")
    if value < 0:
        raise ValueError("не может быть отрицаьельным значением")

def _validate_delivery(value):
    if not isinstance(value, str):
        raise TypeError("не строка")
    allowed_methods = ["самовывоз", "пункт выдачи", "курьер"]
    if value.strip() not in allowed_methods:
        return ValueError(f"не существующий вид доставки, возможны {allowed_methods}")

def _validate_phone(value):
    if not isinstance(value, str):
        raise TypeError("не строка")
    if len(value) != 12:
        raise ValueError("длина неверная")
    if value[0] != "+" :
        raise ValueError("номер должен начинаться с +")
           
