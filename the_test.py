import unittest
import sys

import script_to_test

class TestMath(unittest.TestCase):
	def test_add(self):
		self.assertEqual(script_to_test.add(1, 3), 4)
	def test_minus(self):
		self.assertEqual(script_to_test.minus(1, 1), 0)

if __name__ == '__main__':
	math_test = unittest.TestLoader().loadTestsFromTestCase(TestMath)
	unittest.TextTestRunner(stream=sys.stdout).run(math_test)


