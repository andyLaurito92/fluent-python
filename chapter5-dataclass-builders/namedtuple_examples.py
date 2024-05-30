from collections import namedtuple
import json

Coordinates = namedtuple('Coordinates', ['latitude', 'longitude'])
City = namedtuple('City', ['name', 'population', 'country', 'coordinate'])

buenos_aires = City('Buenos Aires', 2891000, 'AR', Coordinates(-34.61, -58.38))

print(buenos_aires)

germany_data = ('Germany', 83000000, 'DE', Coordinates(51.16, 10.45))

"We can build named tuples in runtime"
germany = City._make(germany_data)
print(germany.coordinate)
print(germany._asdict())

"""
Useful to know for sending data to a JSON API
"""
json.dumps(germany._asdict())


sao_pablo = ('Sao Pablo', 12325232, 'BR', Coordinates(-23.55, -46.63))
# Another way of building in runtime a city instead of using _make
sao_pablo_city = City(*sao_pablo)
