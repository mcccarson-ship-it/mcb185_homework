
# find all pythagorean triples under 100

import math

for a in range(1, 101):
	for b in range(a, 101):
		c = math.sqrt(a**2 + b**2)
		if c % 1 == 0 and c <= 100:
			print(int(a), int(b), int(c))
