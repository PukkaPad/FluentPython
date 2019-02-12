import unittest
from StrKeyDict0 import StrKeyDict0

class Test(unittest.TestCase):
	def setUp(cls):
		cls.d = StrKeyDict0([('2', 'two'), ('4', 'four')])

	def testGet(self):
		assert self.d['2'] == 'two'

	def testReturnKeyError(self):  
		self.assertRaises(KeyError, self.d.get('1'))

	def testIn(self):
		t = 2 in self.d
		self.assertTrue(t)

	def testNotIn(self):
		f = 1 in self.d
		self.assertFalse(f)

# python3 -m nose -v StrKeyDict0_nosetests.py --processes 4 &>logTests_StrKeyDict0.txt

