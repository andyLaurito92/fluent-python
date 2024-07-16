"""
Strategy pattern: Define a family of algorithms, encpasulate each one, and make them
interchangeable. Strategy lets the algorithm vary independently from
clients that use it.
"""

"""
For this example, we model discounts in orders according to the
attributes of the customer or inspection of the oredered items

Elements in pattern:

Context: Provides a service by delegating some cmoputation to intercheangable
components that implement alternative algorithms

Strategy: Interface in common to the components that implement the different algorithms

Concrete strategies: One of the concrete subclasses of Strategy

Note: The selection of the strategy is outside the scope of the pattern
"""
from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional

class Customer(NamedTuple):
    name: str
    fidelity: int

class LineItem(NamedTuple):
    product: str
    quantity: int
    price:int

    def total(self) -> Decimal:
        return self.price * self.quantity

class Order(NamedTuple): # Context
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional['Promotion'] = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total(): .2f} due: {self.due():.2f}>'


class Promotion(ABC): #Strategy
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        """Return discount as a positive dollar amount"""


class FidelityPromo(Promotion): #Concrete strategy
    """5% discount for customers with 1000 or more fidelity points"""

    def discount(self, order: Order) -> Decimal:
        return order.total() * Decimal('0.05') if order.customer.fidelity >= 1000 else Decimal(0)


class BulkItemPromo(Promotion): #Concrete strategy
    """10% discount for each LineItem with 20 or more units"""

    def discount(self, order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal('0.1')
        return discount


class LargeOrderPromo(Promotion): #Concrete strategy
    """7% discount for orders with 10 or more distinct items"""

    def discount(self, order) -> Decimal:
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * Decimal('0.07')
        return Decimal(0)


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = (LineItem('banana', 4, Decimal('.5')),
        LineItem('apple', 10, Decimal('1.5')),
        LineItem('watermelon', 5, Decimal(5)))

Order(joe, cart, FidelityPromo())

Order(ann, cart, FidelityPromo())

banancart = (LineItem('banana', 30, Decimal('.5')),
             LineItem('apple', 10, Decimal('1.5')))

Order(joe, banancart, BulkItemPromo())

longcart = tuple(LineItem(str(sku), 1, Decimal(1)) for sku in range(10))

print(Order(joe, longcart, LargeOrderPromo()))

Order(joe, cart, LargeOrderPromo())


"""
The above implements the strategy pattern, but there are some bolierplate code
that can be removed:

1. Each concrete strategy is a class with a single method. Why not just use a function?
2. The concrete strategies are stateless. Why not use a shared instance?

Let's rewrite the above code and remove the above bolierplate code
"""
