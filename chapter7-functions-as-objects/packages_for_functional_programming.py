from functools import reduce
from operator import mul

def factorial(n):
    return reduce(lambda a, b: a * b, range(1, n+1), 1)

factorial(5)

"""
There's no need to implement the anonymous multiply function!
In the operator package, we have a lot of operator functions
"""

def factorial2(n):
    return reduce(mul, range(1, n+1), 1)

factorial2(5)

from operator import itemgetter

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Beijing', 'CN', 20.463, (39.913889, 116.391667)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ('Buenos Aires', 'AR', 19.429, (-34.603333, -58.381667)),
]

"""
Sort by city. If we wouldn't use itemgetter, we would have to use a lambda function
such as: lambda city: city[0]
"""
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)


"""
Using item getter to get the first two elements of the tuple
"""
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))


"""
itemgetter uses the [] operator. This means that we can use it with any object that implements
the [] operator. This is the case of classes that implement the __getitem__ method.
"""

from collections import namedtuple
from operator import attrgetter

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')

metro_areas = [Metropolis(name, cc, pop, LatLong(lat, lon))
               for name, cc, pop, (lat, lon) in metro_data]

print(f"Lat coordinate for first metropolitan area: {metro_areas[0].coord.lat}")

name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))


"""
List of functions that we have in operator module
"""
import operator
print(' '.join([fun for fun in dir(operator) if not fun.startswith('__')]))
