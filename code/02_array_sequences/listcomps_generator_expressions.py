# -*- coding:utf-8 -*-
import timeit
import array

# which is easier to read?

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
	codes.append(ord(symbol))

print(codes)

print('#######')

codes = [ord(symbol) for symbol in symbols]

print(codes)

print('\n')

# listcomps x map and filter
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

print('########')

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

print(beyond_ascii)

## speed:
TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""

def clock(label, cmd):
	res = timeit.repeat(cmd, setup=SETUP, number = TIMES)
	print(label, *('{:.3f}'.format(x) for x in res))

clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')

# Cartesian products
colours = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(colour, size) for colour in colours 
						for size in sizes]
print(tshirts)
print('\n')
for colour in colours:
	for size in sizes:
		print((colour, size))
print('\n')

# Generator Expressions
print('Initializing a tuple:\n')
print(tuple(ord(symbol) for symbol in symbols))
print('Initializing an array:\n')
print(array.array('I', (ord(symbol) for symbol in symbols)))
print('\n')
## genexp with a Cartesian product to print out a roster of T-shirts of two colors in three sizes.
for tshirt in ('%s %s' % (c, s) for c in colours for s in sizes):
	print(tshirt)


