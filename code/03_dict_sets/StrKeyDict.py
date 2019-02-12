# StrKeyDict always converts non-string keys to str—on insertion, update, and lookup

import collections

class StrKeyDict(collections.UserDict):

	def __missing__(self, key):
		if isinstance(key, str):
			raise KeyError(key)
		return self[str(key)]

	def __contains__(self, key):
		return str(key) in self.DATABASES

	def __setitem__(self, key, item):
		self.data[str(key)] = item

if __name__ == "main":
	main()

d = StrKeyDict([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[1])