# fermat.py

A small Python script based on mathematical work of Pierre de Fermat.

## How to Use

Downloaded or clone these scripts, change your directory to that location. Then type the following command into your CLI to run the basic unit test:

```python
python test.py
```

Or type the following to run the main file. Then you can run test() to view the returned strings from the main functions in the file:

```python
python fermat.py
```

## fermat.py Functions

The following functions are available in fermat.py:

- `isPrime(n)` - A helper function for getFermatPrimes. Answers the expected "is n prime" question.

- `getFermatPrimes(n)` - Finds and returns all Fermat primes (primes of the form 2^(2^k) + 1) up to and including the positive integer n. Note: only 5 are currently known to exist.

- `getDiaphantineSums(n, degree=2)` - Finds and all positive integer solutions a and b to a^2 + b^2 = n^2 for the given n, and returns all those triplets that end with n (i.e., (a, b, n) and (b, a, n)). Note: by Fermat's Last Theorem, this is impossible when degree is an integer bigger than 2.

- `guessPrimality(n, trials=3)` - Based on Fermat primality test (not for practical use), performs test on`trials` random integers less than n, using Fermat's Little Theorem to try and determine if n is composite or (most likely) prime.
