"""
I announced the Python's Advent Calendar challenge on Nov 28th at 14:56 CET. The deadline for signing up 
was Dec 1st 00:00 CET. Write a function called take_difference(datetime1, datetime2), which receives as 
arguments 2 `datetime.datetime` objects (assume datatime1 < datatime2) and computes the time differnce 
between datetime2 and datetime1 in seconds (as integer). Use this function to compute how much time 
(in seconds) did you have for joining the challenge :) Print the result! If you are able to, 
write another function called take_difference2 that takes an additional argument called `unit` (str), 
which is 'second' per default but can also be 'hour' or 'miunte', and if specified, returns the mentioned
 time difference in a given unit.


"""
from datetime import datetime

datetime1 = datetime(2019,11,28,14,56,00)
datetime2 = datetime(2019,12,1,00,00,00)

#(datetime (year, month, day, hour, minute, second))
def take_difference(datetime1, datetime2):
	differenceDatetime = datetime2 - datetime1
	diffSeconds = differenceDatetime
	return 'The time diference is {} seconds'.format( diffSeconds.seconds )

print(take_difference(datetime1, datetime2))


"""


# For begginers:
def take_difference(datetime1, datetime2):
  return int((datetime2-datetime1).total_seconds())

testyourcode.check_funcion(take_difference)

# For advanced:

def take_difference2(datetime1, datetime2, unit='second'):
    outp_true=int((datetime2-datetime1).total_seconds())
    if unit=='minute':
      outp_true=int(outp_true/60)
    elif unit=='hour':
      outp_true=int(outp_true/3600)
    return outp_true

"""
