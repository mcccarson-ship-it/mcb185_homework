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

def circle_area(r): return math.pi * r**2
def rectangle_area(w,h): return w * h

print(circle_area(5))
print(rectangle_area(4,10))

s = 'hello world'
print(s, type(s))

a = 2
b = 2
if a == b:
	print('a equals b')

def is_even(x):
	if x % 2 == 0: return True
	return False

print(is_even(2))
print(is_even(3))

if a < b:
	print('a < b')
elif a > b:
	print('a > b')
else:
	print('a == b')

if math.isclose(a, b): print('close enough')

