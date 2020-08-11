def dash():
	print("-" * 20)

import math
#print(dir(math))


dash()
dash()

import random
#print(dir(random))

print(random.randint(1,100))

dash()
dash()

import time
#print(dir(time))

print(time.tzname)


dash()
dash()
dash()


import calendar
#print(dir(calendar))
print(calendar.prmonth(2020, 8))

dash()
dash()

import os
for file in os.listdir("/home"):
	print(file)

for file in os.listdir("."):
	print(file)
