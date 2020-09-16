import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import api

class TestApi(unittest.TestCase):

	def test_request_and_store1(self):
		api.load_config()
		result = api.request_and_store("3448433")
		self.assertEqual(result['name'], "São Paulo")

	def test_request_and_store2(self):
		api.load_config()
		result = api.request_and_store("1234567")
		self.assertEqual(result['cod'], "404")

	def test_get_weather1(self):
		api.load_config()
		result = api.get_weather("3448433")
		self.assertEqual(result['name'], "São Paulo")

	def test_get_weather2(self):
		api.load_config()
		result = api.get_weather("1234567")
		self.assertEqual(result['cod'], "404")

if __name__ == '__main__':
	unittest.main()