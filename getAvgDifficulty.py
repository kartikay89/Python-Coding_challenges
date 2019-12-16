"""
While submitting each task I ask you "how difficult was this it?" in order to adjust the difficulty level of
next tasks. Write a function called get_avg_difficulty(list_of_lists) that takes as input a list of lists , 
for example l = [[1,0,8,4], [2, 5, 6, 2], [8,8,1,7], ..., [1,9,4,5]] where each list in l shows the difficulty 
scores for 1 tasks, and returns the average difficulty score given by all participants for all 
len(list_of_lists) tasks (as float). Assume that the length of each of the sublists is same. If you are able 
to (hope you are!), write an additional function called get_median_difficulty(list_of_lists) that returns the 
median instead of the average of the difficulty scores

"""

# Average difficulty score
def get_avg_difficulty(list_of_lists):
	avgScores = [[scores for scores in row] for row in list_of_lists]
	avgSums = [sum(scores) / len(scores) for scores in avgScores]
	return avgSums
  
l = [[1,0,8,4], [2, 5, 6, 2], [8,8,1,7], [1,9,4,5]] 
print(get_avg_difficulty(l))

# Median difficulty score
from statistics import median

def get_median_difficulty(list_of_lists):
	medScores = [[scores for scores in row] for row in list_of_lists]
	medSums = [median(scores) for scores in medScores]
	return medSums

print(get_median_difficulty(l))

"""

l = [[1,0,8,4], [2, 5, 6, 2], [8,8,1,7], [1,9,4,5]] 
print(get_avg_difficulty(l))
testyourcode.check_funcion(get_avg_difficulty)

# advanced
def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0
        
def get_median_difficulty(list_of_lists):
  all_scores = []
  for subl in list_of_lists:
    all_scores = all_scores + subl
  return median(all_scores)
  
print(get_median_difficulty(l))


"""
