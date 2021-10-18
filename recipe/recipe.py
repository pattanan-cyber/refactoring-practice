"""
Recipe for a hot beverage that the CoffeeMaker can make.
A recipe can contain coffee, sugar, milk, chocolate, and water.
Units are not specified.
"""
from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    coffee: int
    chocolate: int
    milk: int
    sugar: int
    price: float

    def __init__(self, name, coffee=0.0, chocolate=0.0, milk=0.0, sugar=0.0, price=0.0):
        self.name = name
        self.coffee = coffee
        self.chocolate = chocolate
        self.milk = milk
        self.sugar = sugar
        self.price = price
