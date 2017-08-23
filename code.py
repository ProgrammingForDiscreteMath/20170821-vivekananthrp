# Create a list with the first ten triangular numbers
# (see https://oeis.org/A000217)

from sage.all import *


L = [i for i in range(10)]

# Create a function to test if a number is prime
def is_prime(n):
	return n in Primes()

# Tests

print 'Check Prime\n'
print is_prime(2033) == False
print is_prime(2039) == True
print is_prime(10) == True

# Create a function which returns a list of the first ten prime numbers
# greater than or equal to n

def next_ten_primes(n):
	ten_primes=[]
	ten_primes.append(n)
	for i in L:
		ten_primes.append(next_prime(ten_primes[-1]))
	return ten_primes

print '\nNext ten primes\n'
print next_ten_primes(2033)
print next_ten_primes(2039)

# Tests
# next_ten_primes(2033) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]
# next_ten_primes(2039) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]



print ('_'*100+'\n')


