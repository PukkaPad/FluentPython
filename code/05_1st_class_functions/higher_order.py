# Higher-Order Functions
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key = len)) # Any one-argument function can be used as the key.

## Sorting a list of words by their reversed spelling
def reversing(word):
	return word[::-1] # s[start:stop:step]

print(reversing('testing'))
print(sorted(fruits, key = reversing))

## Modern Replacements for map, filter, and reduce
# since the introduction of list comprehensions and generator ex‐ pressions, they are not as important
from func_obj import factorial as fact

print(list(map(fact, range(6))))
print("\n")
print([fact(n) for n in range(6)])
print("\n")
print(list(map(fact, filter(lambda n: n % 2, range(6)))))
print([fact(n) for n in range(6) if n % 2])
print("\n")
# Sum of integers up to 99 performed with reduce and sum
from functools import reduce
from operator import add
print(reduce(add, range(100)))
print(sum(range(100)))