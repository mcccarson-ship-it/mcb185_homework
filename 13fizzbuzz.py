
for i in range(0, 101):
	s = ''
	if   i % 15 == 0: s = 'fizzbuzz'
	elif i %  3 == 0: s = 'fizz'
	elif i %  5 == 0: s = 'buzz'
	print(i, s)
