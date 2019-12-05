"""

Write a function called fun_with_words(word) that takes as input a word (string) and returns a new word 
that is a combination of the given word and of its reverse. For example, calling 
fun_with_words('TrAvElInGpRoGrAmMeR'), one should get the following output 
'TrAvElInGpRoGrAmMeRReMmArGoRpGnIlEvArT'. If you are not a beginner, write an additional function called 
fun_with_words2(word) that does the same but also removes all vowels from the resulting string.

"""

def fun_with_words(word):
	reverseWord = word[:: -1]
	vowels = ['a','e','i','o','u']

	for words in reverseWord.lower():
		if words in vowels:
			reverseWord = reverseWord.replace(words, "")
			return reverseWord

print(fun_with_words('Kartikay'))


"""
# beginners
def fun_with_words(word):
  return word+word[::-1]
  
# advanced 
import re
def fun_with_words2(word):
  new_word=fun_with_words(word)
  for vowel in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    new_word = new_word.replace(vowel, '')
  return new_word

"""