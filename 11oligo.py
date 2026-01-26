
def calculate_oligo_tm(a, c, g, t):
	total_len = (a + c + g + t)
	gc_count = (g + c)
	at_count = (a + t)

	if total_len <= 13:
		tm = (at_count * 2) + (gc_count * 4)
	else:
		tm = 64.9 + 41 * (gc_count - 16.4) / total_len

	return tm

result = calculate_oligo_tm(5, 7, 3, 4)
print(result)


