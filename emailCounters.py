"""

Let's suppose we want to analyse the email addresses which participants of this challenge 
used for registration. Write a function called check_domains(list_of_emails) that takes as 
input a list of email addresses (strings) and returns a Counter (if you don't know what a 
Counter is, please go to the resources first) showing the number of email addresses by 
domain (the part that comes after '@').

"""
import re
from collections import Counter

listOfEmails = ['abc@gmail.com', 'abc@yahoo.com', 'abc@yahoo.nl', 'abc@yahoo.co.in', 'xyz@gmail.com',
'xyz@yahoo.in', 'xyz@yahoo.nl', 'xyz@yahoo.com', 'xyz2@gmail.com', 'kar@yahoo.com', 'xyz@yahoo.co.in, xyz@gmail.com']


# Using the counter module

def check_domains(list_of_emails):
	gmailCounter = 0
	yahooNLCounter = 0
	yahooINCounter = 0
	yahooComCounter = 0

	gmailRegex = r'\bgmail\b'
	yahooNL = r'\bnl\b'
	yahooIN = r'\bin\b'
	yahooCom = r'\byahoo.com\b'
	

	for emails in list_of_emails:
		gmailX = re.findall(gmailRegex, emails)
		if gmailX:
			gmailCounter +=1

		yahoonlX = re.findall(yahooNL, emails)
		if yahoonlX:
			yahooNLCounter +=1

		yahooInX = re.findall(yahooIN, emails)
		if yahooInX:
			yahooINCounter +=1

		yahooCOmX = re.findall(yahooCom, emails)
		if yahooCOmX:
			yahooComCounter +=1

	
	return 'Gmail addresses are: {}, Netherlands yahoo are: {}, Indian Yahoo are: {}, Yahoo.com are: {} '.format(gmailCounter,
		yahooNLCounter, yahooINCounter, yahooComCounter)
	

print(check_domains(listOfEmails))


"""
def check_domains(list_of_emails):
  return Counter([d.split('@')[1] for d in list_of_emails])

emails = ['magda@gmail.com', 'travelingprogrammer@yahoo.com','polishgirl@outlook.com', 'travelingprogrammer@gmail.com']
print(check_domains(emails))


"""

