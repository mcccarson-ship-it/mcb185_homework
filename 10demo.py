# 10demo.py by madeline_carson

print('hello, again') #helllooo

print(1.5e-2)

print(2 ** 6)

print(5 % 2)

print(0.1 * 1)

print(0.1 * 3)

import math

a = 3                         # side of triangle
b = 4                         # side of triangle
c = math.sqrt(a**2 + b**2)    # hypotenuse

print(type(a), type(b), type(c), sep=', ', end='!\n')

def pythagoras(a,b):
	c = math.sqrt(a**2 + b**2)
	return c

print(pythagoras(3,4))
