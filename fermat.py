# A simple Python project based on Pierre de Fermat's mathematical works
# author Tim S. Long

from random import randrange

def isPrime(n):
	"""
	Checks if a natural number is prime

	:param n: the number (a positive integer) being checked
	:return: boolean
	""" 

	# prime larger than sqrt(n) cannot divide n (Number Theory 101)
	cap = int( n**(.5) )

	if n % 2 == 0: # remove the single even case
		return False

	for i in range(3, cap, 2): # ... to run through possible odd divisors
		if n % i == 0:
			return False
	else:
		return True

def getFermatPrimes(n):
	"""
	Finds all "Fermat primes" less than or equal to a given
	integer. Note: these numbers get large quickly, so this is
	not ideal in real use for say, n > 100000. In fact,
	currently the largest known Fermat Prime is 65537.

	:param n: the number (a positive integer) integer being checked
	:return: boolean
	"""

	if n > 100000:
		raise ValueError('''These numbers get large quickly.
		 Let\'s keep it reasonable, ok?''')
		return None

	foundPrimes = []
	k = 0
	fNum = 2**(2**k) + 1

	# Previous method. Deprecated due to memory usage.
		# fermatNumbers = list(map(lambda k: 2**(2**k) + 1, range(1, n+1)))
		# for i in fermatNumbers:
	
	while fNum <= n:
		if isPrime(fNum):
			foundPrimes.append(fNum) # ('2^(2^%s) + 1' % (k), fNum)) is a little messy, but would provide the formula with the number
		k += 1
		fNum = 2**(2**k) + 1

	print('Found all ' + str(len(foundPrimes)) + ' Fermat primes from ' + str(foundPrimes[0]) + ' to ' +  str(foundPrimes[-1]) + ':')
	print("\n".join(str(p) for p in foundPrimes))
	return foundPrimes

def getDiaphantineSums(n, degree=2):
	"""
	Checks if n satisfies n^2 = a^2 + b^2 (a "Diophantine" equation)
	for any two other positive integers a and b (a, b are not necessarily
	distinct). Note: although a different degree than 2 can be passed
	in, this will result in an empty collection returned (as a result
	of Fermat's Last Theorem).

	:param n: the number (a positive integer) we square to get the sum
	:param degree=2: number, the power on the three integers in the equation.
	:return: boolean
	"""

	if degree > 2:
		raise ValueError('No solutions exist for degree > 2 (Ferma\'s Last Theorem) ')

	tuples = []

	for pair in [(a,b) for a in range(1, n+1) for b in range(1, n+1)]:
		if pair[0] ** degree + pair[1] ** degree == n ** degree:
			triplet = list(pair)
			triplet.append(n)
			tuples.append(triplet)

	return tuples

def guessPrimality(n, trials=3):
	"""
	Uses Fermat primality test to give an educated guess on if a number is prime

	:param n: the positive integer being checked for primality
	:param trials=3: the number of random guesses applied in the test
	:return: a string defining if n is composite or (assumed to be) prime
	"""

	for i in range(trials):
		guess = randrange(2, n - 1) # Fermat's test picks from 2 to n - 2 (inclusive)
		if guess**(n - 1) % n != 1:
			return str(n) + " is composite"
	else:
		return str(n) + " is probably prime... probably."

# A simple test to print out some results
def test():
	print( getFermatPrimes(80000) )
	print( getDiaphantineSums(10) )
	print( guessPrimality(231) )