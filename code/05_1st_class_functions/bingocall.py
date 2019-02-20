import random

class BingoCage:
	"""A BingoCage does one thing: picks items from a shuffled list"""

	def __init__(self, items):
		self._items = list(items)
		random.shuffle(self._items)

	def pick(self):
		try:
			return self._items.pop()
		except IndexError:
			raise LookupError('pick from empty BingoCage')

	def __call__(self):
		return self.pick()

if __name__ == "__main__":
	bingo = BingoCage(range(10))
	print(bingo.pick())
	print(bingo())
	print(callable(bingo))
	print("Function inspection (dir): ")
	print(dir(bingo.pick))