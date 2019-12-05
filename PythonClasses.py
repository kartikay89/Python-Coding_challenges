"""

Example 1

"""

""" The example shows a very simple data in a class """

class UserData:
	"""docstring for UserData"""
	def __init__(self, First_Name, last_Name, Age):
		self.FN = First_Name
		self.LN = last_Name
		self.Age = Age


User = UserData("Kartikay", "Singh", 30)
print(User.FN)
print(User.LN)
print(User.Age)
		
"""

Example 2

"""

""" Slightly complex example with a dictionary """
Person = {"First_Name": "Kartikay",
		"last_Name": "Singh",
		"Age": 30}

class person(object):
	def __init__(self, dictionary):
		for key in dictionary:
			setattr(self, key, dictionary[key])


Person = person(Person)
print(Person.First_Name)
print(Person.last_Name)
print(Person.Age)


""" We also see logging """
import logging
