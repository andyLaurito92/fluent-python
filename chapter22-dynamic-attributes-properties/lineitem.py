class LineItem0:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


"""
First problem w/implementation above: weight can be introduced
as negative value
"""

class LineItem1:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight # setter is already in use
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')


item1 = LineItem1("some cool description", 30, 23.3)
