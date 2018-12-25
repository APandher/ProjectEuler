import math 



def palindrome_finder():
	palindromes = []
	for three_digit in range(900,1000):
		for three_digit_2 in range(900,1000):
			newNumstr = str(three_digit*three_digit_2)
			if newNumstr[0]==newNumstr[-1] and newNumstr[1] == newNumstr[-2] and newNumstr[2] == newNumstr[-3]:
				palindromes.append(int(newNumstr))
	return palindromes



#first make a for loop to run through all of the three digit numbers
#then make a nested for loop to multiply each combination
#convert each number into a string and check to see if the first two numbers match the last 2



