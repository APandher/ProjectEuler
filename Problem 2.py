import math 


def fibbonaci():

	fibbonaci_sequence = [1,2]
	for i in range(1,100000):
		next_term = fibbonaci_sequence[-1] + fibbonaci_sequence[-2]
		fibbonaci_sequence.append(next_term)

		if fibbonaci_sequence[-1] >= 4_000_000:
			fibbonaci_sequence.remove(fibbonaci_sequence[-1])
			return fibbonaci_sequence

def main():
	total = 0
	fibbonaci_list = fibbonaci()
	for number in fibbonaci_list:
		if number%2 == 0:
			total += number 

	return total
