"""
I still haven't decided on where I should go in March and I ask you for help!
Write a function called check_destination(city, avg_temp, avg_airbnb_price, time_offset) that
takes as input a city (string), an average (high) temperature in March (float), 
an average monthly AirBnB price (float) and a time offset (int, i.e. 2 means UTC+2), 
and returns 'city is a good destination', i.e. 'Warsaw is a good destination' 
if a city is a good destination for me to go, and 'city is a bad destination' i.e. 
'Warsaw is a bad destination' otherwise. Let's define what a 'good' destination is:
* The average temperature should be above 15 degrees (Celsius)
* The average monthly AirBnB price for an apartment should be max 1000 (Euros but forget 
about the currency)
* The time offset should be between 0 and 8, both inclusive (I hate waking up early!).
Use your function to check if ("Lisboa", 18.5, 1050.90, 0) would be a good destination for me to go 
(just print the result!) :)
If you are advanced, write an additional function called get_local_time(city, time_offset) 
that takes as arguments a city and a time offset, computes local time in given city and 
returns 'It is HH:MM:SS local time in city right now.'

"""
import pytz
from datetime import datetime
from pytz import timezone


def check_destination(city, avg_temp, avg_airbnb_price, time_offset):
	avgTemp = float(avg_temp)
	AvgAirBnbPrice = float(avg_airbnb_price)
	timeOffset = int(time_offset)

	goodMessage = '{} is a good destination' .format(city)
	badMessage = '{} is a bad destination' .format(city)

	# function to get local time of a city / Country
	# def getLocalTime(city):
	# 	cityTime = timezone(city)
	# 	dateTimeCity = datetime.now(cityTime)
	# 	return dateTimeCity

	# localCityTime = getLocalTime(city)

	# good destination conditions
	if avgTemp <= 15 and AvgAirBnbPrice <= 1000 and timeOffset in range(0,8):
		return goodMessage
	elif avgTemp > 15 and AvgAirBnbPrice <= 1000 and timeOffset in range(0,8):
		return badMessage
	elif avgTemp <= 15 and AvgAirBnbPrice > 1000 and timeOffset in range(0,8):
		return badMessage
	elif avgTemp <= 15 and AvgAirBnbPrice <= 1000 and timeOffset not in range(0,8):
		return badMessage
	


	return avgTemp, AvgAirBnbPrice, timeOffset, localCityTime

print(check_destination("Amsterdam", 15, 1000, 6))



"""

# for beginners:

def check_destination(city, avg_temp, avg_airbnb_price, time_offset):
  if all([avg_temp>15, avg_airbnb_price <= 1000, 0 <= time_offset <= 8]):
    return "%s is a good destination." % city
  else:
    return "%s is a bad destination." % city

print(check_destination("Lisboa", 18.5,  1050.90,  0))
testyourcode.check_funcion(check_destination)

# for advanced:
print('----------------------------')
from datetime import datetime, timedelta

def get_local_time(city, time_offset):
  return "It is %s local time in %s right now." % ((datetime.utcnow() + timedelta(hours=time_offset)).strftime("%X"), city)
  
print(get_local_time("Warsaw", 1))



"""