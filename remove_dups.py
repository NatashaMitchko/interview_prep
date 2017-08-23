"""
################################################################################
Name of problem: Remove Duplicates
Problem description: Remove the duplicates in a linked list
################################################################################
"""

"""
################################################################################
First attempt without looking up any answers
################################################################################
"""
def remove_dups(llist):
	""'Remove duplicates from linked list'""
	seen = set()
	current = llist.head
	seen.add(current.data)
	while current not None:
		if current.next.data in seen:
			current.next = current.next.next
			current = current.next
		else:
			seen.add(current.data)
			current = current.next


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
