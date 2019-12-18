"""
One of the questions on the registration form you had to complete was
"How good do you speak Python", remember? ;) Below you will find a sample dictionary 
in the form {'Person': python_skills} representing Python skills assigned to each of the 
participants. Write a function called pick_random_pair(dictionary) that accepts as input 
a dictionary and returns a random pair ('Person', python_skills) from the dictionary. 

For advanced: write additionally a function called pick_random_value_n_times(dictionary, n), 
that picks randomly a value of python_skills n times and returns the average value of 
python_skills of the n samples!


"""
import random

personSkillDict = {
	'Kartikay': 6,
	'Magda': 10,
	'Peter': 8,
	'Dan': 9
}


def pick_random_pair(dictionary):
	name, skills = random.choice(list(dictionary.items()))
	return name, skills

print(pick_random_pair(personSkillDict))


"""
# beginners
def pick_random_pair(dictionary):
  return random.choice(list(dictionary.items())) 
  
dictionary = {'Johny': 2, 'Magda': 10, 'Paul': 7}
print(pick_random_pair(dictionary))
testyourcode.check_funcion(pick_random_pair)

# advanced
def pick_random_value_n_times(dictionary, n):
  levels = [random.choice(list(dictionary.values())) for i in range(0,n)]
  return sum(levels)/len(levels)

print(pick_random_value_n_times(dictionary,10))
"""

