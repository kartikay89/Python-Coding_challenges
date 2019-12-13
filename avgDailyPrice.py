"""
Write a function called compute_average_price(list_of_tuples) that takes as input a list of tuples in form 
(float, int), i.e. [(469.25, 28), (32.44, 2), (35.34, 2)] representing the price (float, 1st element of the tuple) I paid 
for a n-days stay (int, second element of the tuple), and returns the average daily price I paid for the accommodation rounded
to two decimals.
If you are quite advanced, use numpy for that :)


"""

def compute_average_price(list_of_tuples):
	dailyPrice = [price for price, nDays in list_of_tuples]
	return sum(dailyPrice) / len (dailyPrice)

print(compute_average_price([(469.25, 28), (32.44, 2), (35.34, 2)]))

# Same program using numPY
import numpy as np

def computeAvg(list_of_tuples):
	priceData = [price for price, nDays in list_of_tuples]
	PriceDays = np.array([priceData])

	dailyPrice = PriceDays[:]
	print(dailyPrice)
	avgPrice = np.average(dailyPrice)
	return avgPrice

print(computeAvg([(469.25, 28), (32.44, 2), (35.34, 2)]))

"""


def compute_average_price(list_of_tuples):
  return round((sum([el[0] for el in list_of_tuples]) / sum(el[1] for el in list_of_tuples)), 2)



"""