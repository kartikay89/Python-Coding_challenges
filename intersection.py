"""
Among the participants of this challenge there are 3 kinds of people:
a) People who follow me on Instagram to check for challenge updates and didn't want to receive daily tasks reminders,
b) People who don't follow me on Instagram but signed up for receiving daily tasks reminders
c) People who follow me on Insta AND want to receive daily emails.

Write a function called fun_with_sets(set1, set2) that takes as input two sets of participants' IDs: set1 is 
following me on Insta, and set2 is subscribed for getting daily reminders per email. The same participant ID could 
be in both sets. The function should return the total number of participants described by c) as integer.
If you are able to, do it without using the intersection function:)

"""

# a) People who follow me on Instagram to check for challenge updates and didn't want to receive daily tasks reminders
instaNotMail = set(['A', 'B', 'C', 'D', 'E'])
# print(instaNotMail)

# b) People who don't follow me on Instagram but signed up for receiving daily tasks reminders
mailNotInsta = set(['A', 'B', 'E', 'F', 'G', 'H', 'I'])


# Intersection
# def fun_with_sets(set1, set2):
#   return set1.intersection(set2)

# print('People who follow both on insta and email are: {}' .format(fun_with_sets(instaNotMail, mailNotInsta)))



def fun_with_sets(set1, set2):

	allPeople = set1 & set2
	return 'There are {} people who follow both on instagram and mail. There names are {}' .format(len(allPeople), allPeople)


print(fun_with_sets(mailNotInsta, instaNotMail))