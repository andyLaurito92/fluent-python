"""
Context is the same than before, but this time instead of defining classes we will
use functions
"""

from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional, Callable

class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: int

    def total(self) -> Decimal:
        return self.price * self.quantity


class Order(NamedTuple): # Context
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Callable[[Order], Decimal]

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total(): .2f} due: {self.due():.2f}>'


def fidelity_promo(order: Order) -> Decimal:
    """5% discount for customers with 1000 or more fidelity points"""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)
    

def bulk_item_promo(order: Order) -> Decimal:
    """10% discount for each LineItem with 20 or more units"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount

def large_order_promo(order: Order) -> Decimal:
    """7% discount for orders with 10 or more distinct items"""
    distinct_iteams = {item.product for item in order.cart}
    if len(distinct_iteams) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = (LineItem('banana', 4, Decimal('.5')),
        LineItem('apple', 10, Decimal('1.5')),
        LineItem('watermelon', 5, Decimal(5)))

print(Order(joe, cart, fidelity_promo))

print(Order(ann, cart, fidelity_promo))

banancart = (LineItem('banana', 30, Decimal('.5')),
             LineItem('apple', 10, Decimal('1.5')))

print(Order(joe, banancart, bulk_item_promo))

longcart = tuple(LineItem(str(sku), 1, Decimal(1)) for sku in range(10))

print(Order(joe, longcart, large_order_promo))

Order(joe, cart, large_order_promo)


"""
Let's assume that we want to select the best promotion for the customer. With
the function oriented approach, we can do something like this:
"""

promos = [FidelityPromo, BulkItemPromo, LargeOrderPromo]

def best_promo(order: Order) -> Decimal:
    """Compute the best discount available"""
    return max(promo.discount(order) for promo in promos)

"""
Problem with the above approach is that we have to remember to add a new promotion
to the promos list. 

Let's see how we can solve this problem using a decorator:
"""

Promotion = Callable[[Order], Decimal]

promos = []


def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo

def best_promo():
    return max(promo(order) for promo in promos)

@promotion
def fidelity(order: Order) -> Decimal:
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * Decimal('0.05') if order.customer.fidelity >= 1000 else Decimal(0)


@promotion
def bulk_item(order: Order) -> Decimal:
    """10% discount for each LineItem with 20 or more units"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount


@promotion
def large_order(order: Order) -> Decimal:
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)
