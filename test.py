# Unit Test for fermat.py
# author Tim S. Long

import unittest
import fermat

class TestFermatMethods(unittest.TestCase):
	"""
	Basic unit test class for the main methods
	in the fermat.py script.
	"""

	def testPrimes(self):
		self.assertEqual(fermat.getFermatPrimes(80000), [3, 5, 17, 257, 65537])

	def testSums(self):
		self.assertTrue(fermat.getDiaphantineSums(10)[0], [6, 8, 10])

	# Note: guessPrimality may randomly vary in its results. Here we
	# force a result making 2 the only value in the range
	def testPrimeGuessing(self):
		self.assertTrue("composite" in fermat.guessPrimality(4, trials=1))

# Check that everything looks legit
if __name__ == '__main__':
	unittest.main()