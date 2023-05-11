from typing import List, Protocol


class Item(Protocol):
    '''Item protocol
        name: item name
        quantity: item quantity 
    '''
    quantity: float
    price: float


class Product:
    def __init__(self, name: str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price


def calculate_total(items: List[Item]) -> float:
    return sum([item.quantity * item.price for item in items])


# calculate total a product list
total = calculate_total([
    Product('A', 10, 150),
    Product('B', 5, 250)
])

# ...

class Stock:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


# calculate total an inventory list
total = calculate_total([
    Stock('Tablet', 5, 950),
    Stock('Laptop', 10, 850)
])

print(total)
