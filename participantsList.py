"""

Write a function called manage_participants(participants_list, to_remove_list, to_add_list) that 
takes as input a list of participants (list of strings), a list of names to be removed from the list 
and a list of names to be added to the list. If either to_remove_list or to_add_list are not empty, 
this function should remove/add all elements specified there from the participants_list. Please make
 sure that you check if a person is in the participants_list before trying to remove her/him. 
 The function should return a sorted, modified participants_list list.
If you are a beginner, assume that if a person with the same name already exists in the participants 
list, you just skip/don't add her/him again.
If you are not a beginner, handle duplicate names in the following way: if i.e. 'John' already exists
in the participants_list and another 'John' should be added, change the name of the 'John' from the 
participants_list to 'John_1' and the name of 'John' added from the to_add_list list to 'John_2'.


"""
participantsList = ['Neville', 'Snape', 'Dumbledore', 'Hagrid', 'Malfoy', 'Harry']
toRemoveList = ['Malfoy']
toAddList = ['Harry', 'Ron', 'Hermione']
chosenOnes = []

def manage_participants(participants_list, to_remove_list, to_add_list):
	for participants in participantsList:
		# print(participants)
		for someone in toRemoveList:
			if someone in participants:
				participantsList.remove(someone)
				chosenOnes.append(participantsList)

	for heros in toAddList:
		if heros not in participantsList:
			participantsList.append(heros)


manage_participants(participantsList, toRemoveList, toAddList)
# print(chosenOnes)
print(sorted(participantsList))

"""

# beginners
def manage_participants(participants_list, to_remove_list, to_add_list):
  new_list = participants_list
  if len(to_remove_list)>0:
    new_list = [p for p in participants_list if p not in to_remove_list]
  if len(to_add_list)>0:
    for p in to_add_list:
      if p not in new_list:
        new_list.append(p)
  return sorted(new_list)

testyourcode.check_funcion(manage_participants)

# advanced
def manage_participants_advanced(participants_list, to_remove_list, to_add_list):
  new_list = participants_list
  if len(to_remove_list)>0:
    new_list = [p for p in participants_list if p not in to_remove_list]
  if len(to_add_list)>0:
    for p in to_add_list:
      if p not in new_list:
        new_list.append(p)
      else:
        new_list = list(map(lambda b: b.replace(p,p+"_1"), new_list))
        new_list.append(p+'_2')
  new_list.sort()
  return sorted(new_list)

"""