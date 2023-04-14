from dataclasses import dataclass

from model.Product import Product

@dataclass
class CartItem:
    product: Product
    quantity: int

