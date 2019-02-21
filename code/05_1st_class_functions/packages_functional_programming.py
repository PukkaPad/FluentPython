from functools import reduce
from operator import mul
from operator import itemgetter
from collections import namedtuple
from operator import attrgetter
from operator import methodcaller
from functools import partial
import unicodedata, functools

# The operator Module

def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


def fact2(n):
    return reduce(mul, range(1, n + 1))

if __name__ == "__main__":
    print(fact(3))
    print(fact2(3))
    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    cc_name = itemgetter(1, 0) # to return tuples with the extracted values
    for city in sorted(metro_data, key=itemgetter(1)):
        # itemgetter(1) returns the item at index 1.
        print(city)
    print ('#############')  
    for city in metro_data:
        print(cc_name(city))
    print('##############')
    LatLong = namedtuple('LatLong', 'lat long') # define LatLomg
    Metropolis = namedtuple('Metropolis', 'name cc pop coord') # define Metrpolis
    metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
    print(metro_areas[0])
    print(metro_areas[0].coord.lat)
    print('############')
    name_lat = attrgetter('name', 'coord.lat')
    for city in sorted(metro_areas, key = attrgetter('coord.lat')):
    	print(name_lat(city))
    print('################')
    s = 'The time has come'
    upcase = methodcaller('upper')
    print(upcase(s))
    hiphenate = methodcaller('replace', ' ', '-')
    print(hiphenate(s))

# Freezing Arguments with functools.partial
triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(1, 10))))


