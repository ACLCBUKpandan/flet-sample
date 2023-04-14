from model.Product import Product


def get_products() -> list[Product]:
    return [

        Product(id='1',
                name='Bread', 
                price=120.0, 
                image='https://imgs.search.brave.com/5XYroozDgo5t6lZhj8Ay0i8PmZ1VcaRKziF6akzb_3k/rs:fit:700:454:1/g:ce/aHR0cHM6Ly9pbWFn/ZXMtY2RuLjlnYWcu/Y29tL3Bob3RvL2FC/WURLR3pfNzAwYi5q/cGc',
                product_type='bread', 
                stocks=10),
        Product(id='2',
                name='Takyon', 
                price=120.0, 
                image='https://imgs.search.brave.com/T1M7oxJh5L8_A8d_Af_HTq2w3lOaWh9yHKBPvuoazds/rs:fit:600:600:1/g:ce/aHR0cHM6Ly9paDEu/cmVkYnViYmxlLm5l/dC9pbWFnZS4xMTE1/OTIwNDYwLjk2MzUv/cG9zdGVyLDUwNHg0/OTgsZjhmOGY4LXBh/ZCw2MDB4NjAwLGY4/ZjhmOC5qcGc',
                product_type='bread', 
                stocks=10),
        Product(id='3',
                name='Ginger Bread', 
                price=502.0, 
                image='https://imgs.search.brave.com/GeZ7fL57cc4JKmXbTa8BsVm52ZbCnbD1CrIWZwMO22A/rs:fit:1080:622:1/g:ce/aHR0cHM6Ly9kb2dl/bXVjaHdvdy5jb20v/d3AtY29udGVudC91/cGxvYWRzLzIwMjAv/MDcvYmFrZXJtYW4t/YmFraW5nLWRvZ2Ut/YnJlYWQuanBn',
                product_type='bread', 
                stocks=10),
    ]


def get_product_by_id(id: int) -> Product | None:
    return

def find_products(query: str) -> list[Product]:
    return []



def create_product(product: Product):
    return

def delete_product(product: Product):
    return

def update_product(product: Product):
    return
