"""
Assume that we have a list of email addresses of participants of this challenge (yours included).
Write a function called check_attempts(list_of_emails, your_email) that takes as input a list 
of these emails and returns a number of attempts required to randomly select your e-mail address 
from this list.

"""

import random

myEmail = 'kartikays89@gmail.com'

listOfEmails = ['abc@gmail.com', 'abc@yahoo.com', 'abc@yahoo.nl', 'abc@yahoo.co.in', 'xyz@gmail.com',
'xyz@yahoo.in', 'xyz@yahoo.nl', 'xyz@yahoo.com', 'xyz2@gmail.com', 
'kar@yahoo.com', 'xyz@yahoo.co.in, xyz@gmail.com', 'kartikays89@gmail.com']

def check_attempts(list_of_emails, your_email):

	emailSelection = random.choice(list_of_emails)
	print(emailSelection)

	if your_email == emailSelection:
		print('This is my email {} '.format(your_email))
	if not your_email == emailSelection:
		print('Sorry, this is not your email')


check_attempts(listOfEmails, myEmail)



