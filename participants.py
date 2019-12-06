"""
Write a function called clean_participants_list(participants) that takes as input a list of people
 who are taking part in Python's Advent Calendar challenge (list of strings), changes the list a bit,
 and returns the second last person from it. Here is how the function should modify the list:
* First, sort it alphabetically in descending order.
* If 'Magda' is in the list, remove her, she is unfortunately cheating since she saw the questions 
before they were published! Such a shame... :)
* Uh, I forgot to add 'Gabby'! She couldn't sign up using the link so I added her manually... 
If she is not on the list yet, please add her in the second place.
Call the function giving as input the sample participants list I provided below to check how 
it behaves :)

"""


def clean_participants_list(participants):
	# Sorted list in descending order.
	sortedList = sorted(challenge_participants, reverse=True)
	print(sortedList)

	# Removing Magda
	sortedList.remove('Magda')

	# adding Gabby to 2nd place
	if 'Gabby' not in sortedList:
		sortedList.insert(1, 'Gabby')
		return sortedList[-2]
  
challenge_participants = ['John', 'Mike', 'Anna', 'Jacob', 'Magda', 'Tomas', 'Peter']

print(clean_participants_list(challenge_participants))