# -*- coding:utf-8 -*-
import os
from collections import namedtuple

# tuples used as records

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), 
('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
	print('%s/%s' % passport) # The % formatting operator understands tuples and treats each item as a separate field.

for country, _ in traveler_ids:
	print(country)

# tuple unpacking
latitude, longitude = lax_coordinates # unpacking
print(latitude)
print(longitude)

print('Quotient %s and remainder %s' % divmod(20, 8))

t = (20, 8)
print(divmod(*t)) # * unpacks

quotient, remainder = divmod(*t)

print(quotient)

print(remainder)

_ , filename = os.path.split('/home/fake_path/pukkapad.txt') # os.path.split() function builds a tuple (path, last_part) from a filesystem path
print(filename)

## Using * to grab excess items
a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)

# Nested Tuple Unpacking
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat', 'lon'))
fmt = '{:15} | {:^9} | {:^9}'
for name, cc, pop, (latitude, longitude) in metro_areas:
	if longitude <= 0:
		print(fmt.format(name, latitude, longitude))

# Named tuples
City = namedtuple('City', 'name country population coordinates') # Two parameters are required to create a named tuple: a class name and a list of field names, which can be given as an iterable of strings or as a single space- delimited string
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
print(City._fields)
LatLon = namedtuple('LatLon', 'lat lon')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLon(28.613889, 77.208889))
delhi = City._make(delhi_data) # City(*delhi_data) would do the same
print(delhi)
print(delhi._asdict())