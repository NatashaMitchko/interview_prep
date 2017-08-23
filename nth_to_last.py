"""
################################################################################
Name of problem: Return Nth to Last item in linked list
Problem description:
################################################################################
"""

"""
################################################################################
First attempt without looking up any answers
################################################################################
"""

def nth_to_last(ll, n):
	if not ll:
		return 0

	index = nth_to_last(ll.next, n) + 1

	if index = n:
		return ll.data
	return index

def kth_to_last(ll, k):
	p1 = ll.head
	p2 = ll.head

	# Move p1 k steps into the list
	while i < k:
		p1 = p1.next
		i += 1

	# Move both until the first hits the end
	while p2 not None:
		p1 = p1.next
		p2 = p2.next

	# The second is k away from the end
	return p2.data

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
