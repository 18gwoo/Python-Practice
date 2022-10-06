#epoch: A date and time from which a computer measures system time
import time

print(time.ctime(0)) #shows us out epoch. Convert a time expressed in seconds since epoch to a readable string. This returns 0 seconds past epoch

print(time.time()) #Returns seconds since epoch. Based on computers time

#retreive current date and time
print(time.ctime(time.time())) #time.time() returns amount of time since epoch. time.ctime then makes this a readable time

print()

time_object = time.localtime() #creates a time object based on current time. Time.localtime() gives us current time time. Can get utc using time.gmtime() instead of time.localtime()
print(time_object) #can be formatted
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) #string format time #these directives are from python website for strftime. name of month, dat, year, hour, minute, seconds
print(local_time)

print()

time_string = "05 October, 2022"
time_object = time.strptime(time_string,"%d %B, %Y") #day, name of month, year
print(time_object) #gives us time object of specific time

print()

#(year, month, day, hours, minutes, secs, #day of week, # day of year, dst
time_tuple = (2022, 10, 5, 21, 00, 0, 2, 0, 0) #time tuple. Representation of a time
time_string = time.asctime(time_tuple) #gets a time representation and makes it readable. can use time.mktime to get seconds since epoch
print(time_string)
