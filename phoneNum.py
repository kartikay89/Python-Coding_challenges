"""
Imagine you met a very good looking guy/girl and managed to get his/her phone number. The phone number has 9 digits but, unfortunately, one of the digits is missing since you were very nervous while writing it down. 
The only thing you remember is that the SUM of all 9 digits was divisible by 10 - your crush was nerdy and that's one of the things you talked about.. :) Write a function called find_missing_digit(pseudo_number) that 
takes as input a phone number made out of 8 digits and one 'x' (it is a string, for example '0123x1234') and returns the missing digit (as int).

"""

pseudoNumber = '0123x1234'

probNumbers = []

def divisibleFunction(sumlist):
	if sumlist % 10 == 0:
		print('True')
		return probNumbers.append(sumlist)
		

def find_missing_digit(pseudo_number):
	replacementNum = list(pseudo_number.replace('x', '4'))
	# print(replacementNum)
	intNums = list(map(int, replacementNum))
	# print(intNums)
	sums = sum(intNums)
	# print(sums)
	divisibleFunction(sums)
	


find_missing_digit(pseudoNumber)
print(probNumbers)


