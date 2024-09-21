"""
When running mypy in this file, see how the error is thrown in the alert_bird function,
but not in the call (meaning this file). This is because alert_bird is recieveing a valid
parameter, duck, which is an instance of Bird
"""
from birds_example import *

duck = Duck()
alert(duck)
alert_duck(duck)
alert_bird(duck)
