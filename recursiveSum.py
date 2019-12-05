"""
Recursive function to sum all elements of a list among themselves

"""

testList = [10, 20, 30, 40, 50]
matchNumber = 50
outputList = []


def recur(testlist, n=0):
	if n == len(testlist):
		yield ()
		return
	for c in recur(testlist, n+1):
		yield c
		yield c+(testlist[n],)
				
outputVariable = recur(testList)
for i in outputVariable:
	print(i)
	sums = sum(i)
	if sums == matchNumber:
		print("true")
