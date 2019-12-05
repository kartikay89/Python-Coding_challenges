from datetime import datetime

def text_message(name,n,last_access_timestamp):
  tasks = str(n)
  datetime_object = str(datetime.now())

  message = "Dear " + name + ", you have solved " + tasks + " tasks so far and your last access was on" + datetime_object
  
  return message

print(text_message("kartikay", 10, 2019))



"""

# beginner

def text_message(name,n):
  return 'Dear {}, you have solved {} tasks so far.'.format(name,n)

print('beginner version:')
print(text_message('John', 5))
print('')

# advanced

import datetime

def text_message_advanced(name, n, last_access_timestamp):
  percentage = n/24*100
#   return(Dear {}, your participation rate was {}% \
# and your last access was on {} at {}.format(name, str(round(percentage, 1)), 
#                                                         last_access_timestamp.strftime("%d-%m-%Y"), 
#                                                         last_access_timestamp.strftime("%I:%M:%S %p")))

# result = text_message_advanced("John", float(5), datetime.datetime(2019,12,6,8,56,1))

# print('advanced version:')
# print(result)


"""