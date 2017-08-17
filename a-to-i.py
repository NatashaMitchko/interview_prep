"""
################################################################################
Name of problem: a to i

Problem description: Given a string that contains digits, convert that string
into an integer without using built in function int()
################################################################################
"""
"""
################################################################################
First attempt without looking up any answers
################################################################################
"""
def a_to_i(str):
	"""Given a string of digits return that value as an integer

		>>> a_to_i("1234")
		1234
	"""
	chars = str.split()
	for i in range(len(str)):
		chars[i] = chars[i].encode("hex")

	# Not sure how to finish this one...
	# .encode("hex") returns another string

	return chars 

def a_to_i2(str):
	"""Given a string of digits return that value as an integer

		>>> a_to_i2("1234")
		1234
	"""
	s2i = {
		'1': 1,
		'2': 2,
		'3': 3,
		'4': 4,
		'5': 5,
		'6': 6,
		'7': 7,
		'8': 8,
		'9': 9,
		'0': 0
	}

	# Splitting out characters
	chars = [str[x] for x in range(len(str))]

	# Replacing the int with it's numerical counterpart
	for i in range(len(chars)):
		chars[i] = s2i[chars[i]]

	# handling 'ones', 'tens', 'hundreds' places
	i = -1
	zeros = 1
	while i >= -len(chars):
		chars[i] *= zeros
		zeros *= 10
		i -= 1

	return sum(chars)

"""
################################################################################
Solution inspired by looking at the solution(s) of others
################################################################################
"""

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED!"
    print
