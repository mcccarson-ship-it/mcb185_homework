
import math

def char_to_prob(symbol, offset=33):
	q_score = ord(symbol) - offset
	probability = 10**(q_score / -10.0)
	return probability
def prob_to_char(probability, offset=33):
	if probability <= 0:
		q_score = 93
	else:
		q_score = round(-10 * math.log10(probability))
	return chr(q_score + offset)

print(char_to_prob('A'))
print(prob_to_char(0.001))
