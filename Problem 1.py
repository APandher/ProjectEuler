import math 

def main():
	total = 0
	end_limit = 1000

	for number in range(1,end_limit):

		if number%3== 0 or number%5 ==0:
			total += number

	return total


#Find the multiples of 3 below 1000

#Find the multiples of 5 below 1000

#Remove duplicates and add the remaining multiples
