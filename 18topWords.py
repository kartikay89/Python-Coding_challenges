"""
Write a function called get_top_words(plain_text, n) that takes as input a plain text 
(string, lowercase, no special characters) and an integer n and returns all words that 
appear at least n times in the plain_text (as a sorted list). For example, calling 
get_top_words("this challenge is like piece of cake for you if you like coding", 2) we 
should get ["like", "you"] since both words "you" and "like" occur at least twice in the 
input text.


"""
from collections import Counter

def get_top_words(string):
	topWords = string.split()
	countWords = len(topWords)
	print('The total number of words in this string are: {}' .format(countWords))

	topCount = Counter(topWords)

	print(topCount)


get_top_words("this challenge is like piece of cake for you if you like coding")