"""

As you might have noticed, every day I send an email with the solution of the previously
submitted task to those of you who have solved it. Write a function called 
send_personalized_email(mapping, email_address) that takes as input a mapping which is a 
Python dictionary in the form {'Name':'email_address'} and an email address (string), and 
returns a personalized message addressed to a person with the given email_address in the 
form "Dear 'Name', congrats on solving the task!". For example, calling 
send_personalized_email({'Magda' : 'travellingprogrammer@gmail.com', ...}, 
'travellingprogrammer@gmail.com') the function should return 
"Dear Magda, congrats on solving the task!".

"""
# emails is a dictionary that will be updated based upon user name and email
emails = {}

def updateDict():
	name = input('Please enter your name: ')
	email_address = input('Please enter your email address: ')

	if not name:
		print('Please enter your name.')
	if not email_address:
		print('Please enter your email address')
	if name:
		if email_address:
			emails[name]=email_address


def send_personalized_email(email_dictionary):
	for key, value in email_dictionary.items():
		print(key, value)
		return 'Dear {}, congrats on solving the task!'.format(key)

updateDict()
# print(emails)
print(send_personalized_email(emails))
