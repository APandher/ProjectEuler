import math

def sum_of_squares():
	total = 0
	for num in range(1,101):
		square_num = num**2
		total += square_num
	return total


def square_of_sums():
	total2 = 0
	for num in range(1,101):
		total2 += num 

	total2 = total2**2

	return total2



def main():
	total = sum_of_squares()
	total2 = square_of_sums()
	newTot = total2-total

	return newTot

