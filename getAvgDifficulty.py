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