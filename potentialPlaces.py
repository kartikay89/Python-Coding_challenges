"""
Write a function called choose_destination(list_of_tuples) that takes as input a list of tuples in 
form (string, boolean), i.e. list_of_tuples=[('Warsaw', False), ('Barcelona', True)], where each 
tuple represents a city and if this city is a good destination for me to go, and returns a sorted 
list of potential places where I could go. If you are advanced, write a 1-line-solution here :)

"""
listOfTuples = [('Warsaw', False), ('Barcelona', True), ('Amsterdam', True), ('India', True), ('Germany', False)]


def choose_destination(list_of_tuples):
	return sorted([city for (city, destination) in list_of_tuples if destination == True])

print(choose_destination(listOfTuples))