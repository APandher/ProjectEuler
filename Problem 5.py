import math

def main():
	counter = 0
	for number in range(100000000,10000000000,20):
		counter = 0
		for mod in range(1,21):
			new = number%mod
			if new == 0:
				counter += 1 
			if new != 0:
				counter = 0
				continue

			while mod == 20 and new == 0 and counter == 20:
				return number 



			
				


					