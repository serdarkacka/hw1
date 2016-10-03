import unittest
from algorithm import sum

class SumTest(unittest.TestCase):

	def test_Sum(self):
		self.assertEqual(sum([10, 20, 30, 40]), 100)

	def test_SumZero(self):
		self.assertEqual(sum([0, 0, 0]), 0)

	def test_SumEmpty(self):
		self.assertEqual(sum([]), 0)

	def test_SumNone(self):
		self.assertEqual(sum(None), 0)

	def test_SumNegative(self):
		self.assertEqual(sum([10, 20, -10]), 20)



	
if __name__ == '__main__':
	unittest.main()
