import re
from unicodedata import name

# Generic Mapping Types

a = dict(one = 1, two = 2, three = 3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)]) 
e = dict({'three': 3, 'one': 1, 'two': 2}) 
print(a==b==c==d==e)

# dict Comprehensions
DIAL_CODES = [
(86, 'China'),
(91, 'India'),
(1, 'United States'),
(62, 'Indonesia'),
(55, 'Brazil'),
(92, 'Pakistan'),
(880, 'Bangladesh'),
(234, 'Nigeria'),
(7, 'Russia'),
(81, 'Japan'),
]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

print({code: country.upper() for country, code in country_code.items()})

# Set Theory
l = ['spam', 'spam', 'eggs', 'spam']
print(set(l))
print(list(set(l)))

# Count occurrences of needles in a haystack, both of type set
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

found = len(set(NEEDLES) & set(HAYSTACK))
print(found)
###
found = 0
for n in NEEDLES:
	if n in HAYSTACK:
		found += 1
print(found)
###
# another way:
found = len(set(NEEDLES).intersection(HAYSTACK))
print(found)

## set literals
s = {1}
print(type(s))
print(s)
print(s.pop())
print(s) # the standard string representation of sets always uses the {...} notation, except for the empty set

print(frozenset(range(10)))

## Set Comprehensions
# Build a set of Latin-1 characters that have the word “SIGN” in their Unicode names
print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})





