import math 


#using sieve of erastothenes

def prime_numbers(n):
	primeList = []
	sieve = [True] * (n+1) 
	for d in range(2,n+1):
		if sieve[d]:
			primeList.append(d)
		for r in range(d,n+1,d):
			sieve[r] = False
	return primeList[10000]



