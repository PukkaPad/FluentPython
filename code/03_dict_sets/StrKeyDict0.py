# StrKeyDict0 converts nonstring keys to str on lookup

class StrKeyDict0(dict):

	def __missing__(self, key):
		if isinstance(key, str):
			raise KeyError(key)
		return self[str(key)]

	def get(self, key, default = None):
		try:
			return self[key]
		except KeyError:
			return default

	def __contains__(self, key):
		return key in self.keys() or str(key) in self.keys()


if __name__ == "main":
	main()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[1])