"""
################################################################################
Name of problem: Route Between Nodes

Problem description: Given a directed graph, design an algorithm to find out
weather there is a route between nodes.
################################################################################
"""
"""
################################################################################
First attempt without looking up any answers
################################################################################
"""
def route_between_nodes(node1, node2, directed_graph):
	"""checks if there is a route between 2 nodes in given a directed graph, 
	returns bool
	- recursive solution, breadth first seems best
	- go in opposite direction if route doesn't exist from 1st to 2nd
	- current node, current adjcentcy list
	"""
	# node1 will update each call while node2 stays the same
	current = node1
	if current.list == []
		return False
	if current = node2:
		return True
	if current != node2:
		for i in current.list:
			route_between_nodes(i, node2, directed_graph)



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
