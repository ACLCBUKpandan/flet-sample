from dataclasses import dataclass


@dataclass
class Product:
    id: str
    name: str
    price: float
    stocks: int
    image: str
    product_type: str
