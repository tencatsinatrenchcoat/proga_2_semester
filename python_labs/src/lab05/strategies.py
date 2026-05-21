from models import HumanCustomer, CorporateCustomer
from base import Customer


def by_wallet_balance(customer):
        return customer._wallet_balance

def by_name(customer):
        return customer._name

def by_email_and_name(customer):
        return (customer._email, customer._name)
    


def filter_is_corporate(customer):
        return isinstance(customer, CorporateCustomer)


def filter_by_balance(sum):
    def predicate(customer):
        return customer._wallet_balance >= sum
    return predicate
