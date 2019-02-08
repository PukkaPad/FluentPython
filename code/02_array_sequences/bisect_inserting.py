import random
import bisect

# Sorting is expensive, so once you have a sorted sequence, it’s good to keep it that way

# Use a constant see to ensure that we see
# the same pseudo-random numbers each time
# we run the loop.
random.seed(1)

# Generate 10 random numbers and
# insert them into a list in sorted
# order.
l = []
for i in range(1, 10):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
    print ('value: %2d position:%2d' % (r, position), l
    )

print('#############################################')

SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
	new_item = random.randrange(SIZE*2)
	bisect.insort(my_list, new_item)
	print('%2d ->' %new_item, my_list)