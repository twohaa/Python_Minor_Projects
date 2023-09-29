# Good Morning Sir


import time
timee = time.strftime('%H:%M:%S')
print(timee)
hour = int(time.strftime('%H'))
# hour= int(input("Enter hour: "))
# print(hour)

# minute = int(time.strftime('%M'))
# print(minute)
# second = int(time.strftime('%S'))
# print(second)

if (hour >= 6 and hour < 12):
    print("Good Morning..")
elif (hour >= 12 and hour < 18):
    print("Good Afternoon..")
elif (hour >= 18 and hour < 20):
    print("Good Evening..")
else:
    print("Good Night..")
