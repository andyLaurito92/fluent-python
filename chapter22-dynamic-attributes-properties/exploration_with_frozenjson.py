from frozenjson import FrozenJSON
from frozenjson2 import FrozenJSON2
from data_loader import data


"""
Using FrozenJSON class which leverages __getattr__ method, we can access
json attributes as keys instead of having to access them as dictionary keys
"""

frozenjson = FrozenJSON(data)

frozenjson.Schedule.events[40].name

dir(frozenjson.Schedule)
