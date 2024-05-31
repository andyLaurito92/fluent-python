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

print(f"Shows fields from numedtuple city -> {City._fields}")  # ('name', 'population', 'country', 'coordinate')

"""
You can define default values for the fields of a named tuple
"""

CityWithDefault = namedtuple('CityWithDefault', ['name', 'population', 'country', 'coordinate'], defaults=['Argentina', Coordinates(-34.61, -58.38)])

buenos_aires_default = CityWithDefault('Buenos Aires', 2891000)
print(buenos_aires_default)

CityWithDefault._field_defaults

"""
Note: You can add methods to a namedtuple, but it's not recommended. It's better to use a dataclass instead.

Having stated the above, let's see how that would look like :)
"""

# Recalling card decks example from chapter 1

Card = namedtuple('Card', ['rank', 'suit'])
FrenchDeck = namedtuple('FrenchDeck', ['cards'])

FrenchDeck.ranks = [str(n) for n in range(2, 11)] + list('JQKA')
Card.suit_values = {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}


def spade_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(Card.suit_values) + Card.suit_values[card.suit]


Card.overall_rank = spade_high
lowest_card = Card('2', 'clubs')
highest_card = Card('A', 'spades')
lowest_card.overall_rank(), highest_card.overall_rank()

"""
This doesn't work with any built-in type, but it does with namedtuples.
"""
