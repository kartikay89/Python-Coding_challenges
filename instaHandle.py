"""
Write a function called check_insta_handle(name) that takes as input a name (string), 
and returns 'Good' if the handle is a good choice and 'Bad' otherwise. Let's define what a 'Good' insta 
handle is:
-No underscores,
-No hyphens,
-No dots at the beginning or at the end of the name,
-Not too long, 20 characters max.
If you are advanced, write an additional function called check_insta_handle2 that does the same as
 the previous one but also includes the following conditions:
-Not a combination of uppercase and lowercase letters (all letter uppercase or all lowercase),
-No digits,
-No following special characters: @!#$%^&*?~:.

"""
import re
from collections import Counter

def check_insta_handle(name):
	instaPass = 'Good'
	instaFail = 'Bad' 

	regex = r"[-,@,_.!#$%^&*?~:1234567890]"

	x = re.findall(regex, name)

	lenName = len(name)
	print(lenName)

	if x and lenName > 20:
		return instaFail

	if not x and lenName > 20:
		return instaFail

	if x and lenName < 20:
		return instaFail

	if not x and lenName <= 20:
		return instaPass

print(check_insta_handle('Kartikaysingh1989_'))