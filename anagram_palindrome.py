"""
################################################################################
Name of problem: Anagram of a Palindrome
Problem description: Is the word an anagram of a palindrome?
################################################################################
"""

"""
################################################################################
First attempt without looking up any answers
################################################################################
"""

def is_anagram_of_palindrome(word):
	"""Determines if the word is an anagram of a palindrome by counting the 
	letters. 
	>>> is_anagram_of_palindrome("a")
	True

	>>> is_anagram_of_palindrome("ab")
	False

	>>> is_anagram_of_palindrome("aab")
	True

	>>> is_anagram_of_palindrome("arceace")
	True

	>>> is_anagram_of_palindrome("arceaceb")
	False
	"""

	letters = {}

	if len(word) == 1 or len(word) == 0:
		return True

	for char in word:
		if char in letters:
			letters[char] -= 1
		else:
			letters[char] = 1

	return sum(letters.values()) in [0, 1]

"""
################################################################################
Notes: This is an O(n^2) solution. 
################################################################################
"""

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
