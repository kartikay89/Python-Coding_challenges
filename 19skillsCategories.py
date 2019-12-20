"""
Previously, we were considering a sample dictionary in the form of {'Person': python_skills}, 
representing Python level skills assigned to each of the participants. Let's call a person whose 
Python skills are 0, 1 or 2 a beginner, an intermediate a person whose skills are between 3 and 7 
(including both), and anyone above that advanced. Write a function called 
split_participants(dictionary) that accepts as input a dictionary and returns 
3 lists (in form ([...], [...], [...])):

1. beginners - showing names of those participants who are defined as beginners 
(e.g. ['A', 'B', 'C']),
2. intermediate - showing Python skills of those participants who are defined as intermediate 
(e.g. [1,2,3])
3. advanced - showing pairs ('Person': python_skills) of those participants who are defined 
as advanced (e.g. [('A', 1), ('B', 2), ('C',3)]).
Find the most efficient way to do this.


"""

# List to filter people according to skills
beginners = []
intermediate = []
advanced = []

skilledPeople = []

# People with skills
personSkillDict = {
	'Kartikay': 6,
	'Magda': 10,
	'Peter': 8,
	'Dan': 9,
	'abc': 2,
	'xyz': 4
}

def spilt_participants(dictionary):
	for keys, values in dictionary.items():
		if values >= 0 and values <= 2:
			beginners.append([keys])

		if values >= 3 and values <= 7:
			intermediate.append([values])

		if values >= 8:
			advanced.append([tuple((keys, values))])


spilt_participants(personSkillDict)

results = zip(beginners, intermediate, advanced)
print(list(results))


# print(skilledPeople)

