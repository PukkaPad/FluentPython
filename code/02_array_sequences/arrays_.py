from array import array
from random import random

# Creating, saving, and loading a large array of floats
floats = array('d', (random() for i in range(10**7)))
# print(id(floats))
print(f'Last element in array is {floats[-1]}') # inspect last element
fp = open('floats.bin', 'wb') # https://docs.python.org/3/library/functions.html#open
floats.tofile(fp) # save array to a binary file
floats2 = array('d') # create an empty array of doubles: https://docs.python.org/3/library/array.html
print(floats2)
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7) # read 10 million numbers from the binary file
fp.close()
print(f'Last number in array 2 is {floats2[-1]}')
print(floats2 == floats)

# Changing the value of an array item by poking one of its bytes
numbers = array('h', [-2, -1, 0, 1, 2]) # C type: signed short; Python type: int
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B') # C: unsigned char; Python: int
print(memv_oct.format)
print(memv_oct)
print(f'Item size {memv_oct.itemsize}')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)

