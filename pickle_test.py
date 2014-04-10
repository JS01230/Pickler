#Pickle Test
import unittest, os, shutil
import time
from pickler import list_pickler, unpickler

		
class PickleTests(unittest.TestCase):
	def setUp(self):
		self.my_list = ['alpha', 'beta', 'gamma', 'unos', 'dos', 'tres', 10, 20, 30]
		self.path = './pickle_temp'
		os.makedirs(self.path)
		self.file = os.path.join(self.path, 'list.pkl')
		
	def my_list_equals_another(self):
		list_pickler(self.file, self.my_list)
		unpickled_list = unpickler(self.file)
		self.assertEqual(self.my_list, unpickled_list)
		
	def tearDown(self):
		shutil.rmtree(self.path)