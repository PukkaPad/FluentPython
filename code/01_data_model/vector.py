# -*- coding: utf-8 -*-
from math import hypot

class Vector2d:
	"""Represents 2d vectors (Euclidean vectors)."""
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Vector (%r, %r)' % (self.x, self.y)

	def __abs__(self):
		"""Return the absolute value of object"""
		return hypot(self.x, self.y)

	def __bool__(self):
		"""It returns False if the magnitude of the vector is zero, True otherwise. The magnitude is converted to a Boolean using bool(abs(self)) because __bool__ is expected to return a boolean"""
		return bool(abs(self))

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector2d(x, y)

	def __mul__(self, scalar):
		return Vector2d(self.x * scalar, self.y * scalar)


v = Vector2d(3, 4)
print(abs(v))
print(bool(v))
print(v)
v2 = Vector2d(2, 4)
v3 = Vector2d(2, 1)
print(v2 + v3)
print(v * 3)
print(abs(v * 3))