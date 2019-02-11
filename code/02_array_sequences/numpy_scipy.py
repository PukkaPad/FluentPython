import numpy as np
from array import array
from random import random
from time import perf_counter as pc
from collections import deque

# Basic Operations

a = np.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = 3, 4
print(a)
print(a[2])
print(a[2,1])
print(a[:, 1])
print(a.transpose())

# floats = array('d', (random() for i in range(10**7)))
# np.savetxt('numpy_floats.txt', floats)
# floats = np.loadtxt('numpy_floats.txt')
# print(floats[-3:])
# floats *= .5
# print(floats[-3:])
# t0 = pc();
# floats /= 3
# print (pc() - t0)
# # np.save('floats-10M', floats)
# floats2 = np.load('floats-10M.npy', 'r+')
# floats *= 6
# floats2[-3:]

# Deques and Other Queues
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3) # Rotating with n > 0 takes items from the right end and prepends them to the left; when n < 0 items are taken from left and appended to the right.
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1) # Appending to a deque that is full (len(d) == d.maxlen) discards items from the other end; note in the next line that the 0 is dropped.
print(dq)
dq.extend([11, 22, 33]) # Adding three items to the right pushes out the leftmost -1, 1, and 2.
print(dq)
dq.extendleft([10, 20, 30, 40]) # Note that extendleft(iter) works by appending each successive item of the iter argument to the left of the deque, therefore the final position of the items is reversed.
print(dq)




















