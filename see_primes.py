import sys

def see_primes(n):

	for i in range(2, n + 1):
		IS_PRIME = True
		for j in range(1, i + 1):
			if i%j == 0 and j != 1 and j != i:
				IS_PRIME = False
		if IS_PRIME:
			yield i
try:
	n = int(input("choose the range of the primes: "))
except ValueError:
	print("the number should be a integer")

primes = see_primes(n)

len_ = []

for obj in primes:
	# print(obj)
	len_.append(obj)

print(f"{len(len_)} primes has been detected")