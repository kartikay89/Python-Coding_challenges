"""

Write a function called count_letters(text, letter), which receives as arguments a text (string) and 
a letter (string), and returns the number of occurrences of the given letter (count both capital and 
small letters!) in the given string. For example, count_letters('trAvelingprogrammer', 'a') should return 2 
and count_letters('trAvelingprogrammer', 'A') should return also 2. If you are quite advanced,
use Regular Expressions or Lambda function here :)


"""

def count_letters(text, letter):
	newText = text.lower()
	result = 0

	for letts in newText: 
		if letter in letts:
			result +=1
	return result
	

print(count_letters("Kartikay", "k"))

"""

import testyourcode

# one possibility
def count_letters(text, letter):
  return text.lower().count(letter.lower())
  
# another possibility
import re
def count_letters2(text, letter):
  return len(re.findall(letter.lower(), text.lower()))

# another possibility
def count_letters3(text, letter):
  return sum(map(lambda x : 1 if letter.lower() in x else 0, text.lower())) 


"""