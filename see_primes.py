import numpy as np

rang = int(input("choose range of the prime-numbers that you wanna see: "))

def see_primes(n):
	primes = []


	for i in range(2,n+1):
		isPrime = True
		for j in range(2, i):

			if yield i%j == 0:
				isPrime = False

		if isPrime:
			primes.append(i)

	return primes


print(see_primes(rang))