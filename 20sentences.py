"""

Write a function called generate_sentences(subjects, verbs, objects) that accepts as 
input 3 lists: of subjects, e.g. ["I", "You"], verbs, e.g. ["love", "like"], and objects, e.g.
["Python", "coding"], and returns a sorted list of all sentences where subject is in subjects 
and verb is in verbs and object is in objects. Each sentence should end with a ",".


"""
subjectsList = ["I", "You"]
verbsList = ["love", "like"]
objectsList = ["Python", "coding"]


variationsOne = []
variationsTwo = []
variationsThree = []
variationsFour = []

sentenceList = []


# Element extractor zero element
def elementExtractorZero(listOne, listTwo, listThree):
	listOneIndexZero = listOne[0]
	listTwoIndexZero = listTwo[0]
	listThreeIndexZero = listThree[0]

	return listOneIndexZero, listTwoIndexZero, listThreeIndexZero

def generate_sentences(subjects, verbs, objects):
	extractData = elementExtractorZero(subjectsList, verbsList, objectsList)
	return variationsOne.append(extractData)

generate_sentences(subjectsList, verbsList, objectsList)

# Element extractor first element
def elementExtractorFirst(listOne, listTwo, listThree):
	listOneIndexOne = listOne[1]
	listTwoIndexOne = listTwo[1]
	listThreeIndexOne = listThree[1]

	return listOneIndexOne, listTwoIndexOne, listThreeIndexOne

def generate_sentences(subjects, verbs, objects):
	extractData = elementExtractorFirst(subjectsList, verbsList, objectsList)
	return variationsTwo.append(extractData)
	
generate_sentences(subjectsList, verbsList, objectsList)


# Element extractor zeros and first element
def elementExtractorFirst(listOne, listTwo, listThree):
	listOneIndexZerosOne = listOne[0]
	listTwoIndexZerosOne = listTwo[0]
	listThreeIndexZerosOne = listThree[1]

	return listOneIndexZerosOne, listTwoIndexZerosOne, listThreeIndexZerosOne

def generate_sentences(subjects, verbs, objects):
	extractData = elementExtractorFirst(subjectsList, verbsList, objectsList)
	return variationsThree.append(extractData)
	
generate_sentences(subjectsList, verbsList, objectsList)


# Element extractor firsts and zero element
def elementExtractorFirst(listOne, listTwo, listThree):
	listOneIndexOnesZero = listOne[1]
	listTwoIndexOnesZero = listTwo[1]
	listThreeIndexOnesZero = listThree[0]

	return listOneIndexOnesZero, listTwoIndexOnesZero, listThreeIndexOnesZero

def generate_sentences(subjects, verbs, objects):
	extractData = elementExtractorFirst(subjectsList, verbsList, objectsList)
	return variationsFour.append(extractData)
	
generate_sentences(subjectsList, verbsList, objectsList)

# Variation One
firstVariation = [' '.join(i) for i in variationsOne]
# print(firstVariation)

# Variation Two
secondVariation = [' '.join(i) for i in variationsTwo]
# print(secondVariation)

# Variation Three
thirdVariation = [' '.join(i) for i in variationsThree]
# print(thirdVariation)

# Variation Four
fourthVariation = [' '.join(i) for i in variationsFour]
# print(fourthVariation)



# sorted sentence list
sentenceList.append([firstVariation])
sentenceList.append([secondVariation])
sentenceList.append([thirdVariation])
sentenceList.append([fourthVariation])

print(sorted(sentenceList))
