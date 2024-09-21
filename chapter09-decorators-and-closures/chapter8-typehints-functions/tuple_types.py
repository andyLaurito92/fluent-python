"""
Examples on how to use types with tuples
"""

"""
1. Tuple as records
"""

"""
Note: The comment # type: ignore is used to ignore the error that mypy will throw
Try deleting the comment to see the error mypy will throw
"""

from geolib import geohash # type: ignore

PRECISION = 5

def geo_hash(lat_lon: tuple[float, float]) -> str:
    return geohash.encode(*lat_lon, PRECISION)

shanghai = (31.2304, 121.4737)

print(geo_hash(shanghai))


"""
2. Tuple as records with name fields --> Used NamedTuple
"""

from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float


def geo_hash2(lat_lon: Coordinate) -> str:
    return geohash.encode(lat_lon.lat, lat_lon.lon, PRECISION)

shanghai = Coordinate(31.2304, 121.4737)

print(geo_hash2(shanghai))


"""
3. Tuples as immutable sequences -> Use tuple[T, ...]

Note: There is no way to specify fields of different types for
tuples of arbitrary length. 
"""

def sum_immutable_sequence(numbers: tuple[int, ...]) -> int:
    return sum(numbers)

print(sum_immutable_sequence((1, 2, 3, 4, 5)))
