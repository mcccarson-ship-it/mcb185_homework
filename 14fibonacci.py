
# fibonacci sequence = each element is the sum
# of the two numbers that precede it

# initialize the first two numbers
a, b = 0, 1

for _ in range(10):
	print(a, end = ' ')
# update variables: a becomes the previous b,
# and b becomes the sum of the previous two numbers
	a, b = b, a + b
