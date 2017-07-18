"""
################################################################################
Name of problem: Balanced Parentheses
Problem description:
	Given a string, check to see if the parentheses are balanced.
################################################################################
"""

"""
################################################################################
First attempt without looking up any answers
################################################################################
"""

class StackEmptyError(IndexError):
	"""Can not pop off an empty stack"""

class Stack(object):
	"""Simple stack with push and pop methods"""

	def __init__(self):
		"""Initialize the stack with a node"""

		self._lst = []
		self.length = 0

	def push(self, item):
		"""Adds a node onto the stack"""

		self._lst.append(item)
		self.length += 1

	def pop():
		"""Removes the last Node on the stack"""

		if not self._lst:
			raise StackEmptyError

		self.length -= 1
		return self._lst.pop()

	def peek(self):
		"""Reveal the top of the stack"""

		return self._lst[-1]

	def is_empty(self):
		"""Checks is the stack is empty"""

		return not bool(self._lst)

	def __iter__(self):
		"""Allows for iteration over the stack"""
		while True:
			try:
				yield self.pop()
			except StackEmptyError:
				raise StopIteration

	def __repr__(self):
		if not self._lst:
			return "<Stack Empty>"
		else:
			return "<Stack, Length:{}, Tail:{}>".format(self.length, self._lst[-1])


def opposite_char(string):
    """takes on side of a paren and gives the other side
    sidedness matters"""
    opposties = {
    	'(':')',
    	')':'(',
    	'{':'}',
    	'}':'{',
    	'[':']',
    	']':'[',
    	'<':'>',
    	'>':'<'
    }
    return opposties[string]

def is_balanced(s):
	"""Takes a string and checks to see if the parentheses are balanced. Checks for
	(), [], {}, <>

	>>> is_balanced("abcd()")
	True
	>>> is_balanced(")))")
	False
	>>> is_balanced("(")
	False
	>>> is_balanced("abcd")
	True
	"""

	opening = ["(", "{", "[", "<"]
	closing = [")", "}", "]", ">"]

	parens = Stack()

	for char in s:
		if s in opening:
			parens.push(s)
		elif s in closing and parens.is_empty():
			print 'hi'
		elif s in closing and s == opposite_char(parnes.peek()):
			parens.pop()
	if parens.is_empty():
		return True
	return False



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
