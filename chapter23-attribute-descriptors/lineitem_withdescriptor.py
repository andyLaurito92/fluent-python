import logging

logging.basicConfig(level=logging.INFO)

class Quantity:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name
        
    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value should be a number")
        elif value < 0:
            raise ValueError("Value cannot be less than 0")
            
        setattr(obj, self.private_name, value)
                    

    
class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


try:
    wrong_item = LineItem('Testing descriptors', 30, -3)
except ValueError as e:
    logging.info("Error raised " + str(e))


bananas = LineItem("bananas", 3, 8)

print(bananas.price)
print(bananas.weight)
