
 # write a program that simulates saving throws against
 # DCs of 5, 10, and 15

import random

for i in range(1,21):
	d = random.randint(1,20)
	if d >= 5:
		print('succeed')
	else:
		print('fail')

