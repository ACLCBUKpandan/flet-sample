from dataclasses import dataclass

from model.Cart import CartItem
from model.User import User

@dataclass
class Transaction:
    id: str
    cashier: User
    cart_items: list[CartItem]
    date_created: str



