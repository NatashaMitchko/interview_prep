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
# This solution is one where the method is defined on the Graph class itself
class Node(object):
	"""Node for Graph"""

	def __init__(self, name, adjacent=None):
		"""Create a node with a name and optional adjcentcy list"""

		if adjacent is None:
			adjacent = set()

		assert isinstance(adjacent, set), \

		self.name = name
		self.adjacent = adjacent

	def __repr__(self):
		return "<{} Node>".format(self.name)

class Graph(object):
	"""Directed graph with is_reachable method"""

	def __init__(self):
		self.nodes = set()

	def __repr__(self):
		return "<{}>".format([n.name for n in self.nodes])

	def add(self, item):
		self.nodes.add(item)

	def add_relation(self, item1, item2):
		"""adds relation in one direction"""
		item1.adjacent.add(item2)

	def is_reachable(self, node1, node2, seen=None):
		"""Checks if you can get from node1 to node2
		This is depth first.
		"""
		if not seen:
			seen = set()

		if node1 is node2:
			return True

		seen.add(node1)

		for node in node1.adjacent - seen:
			if self.is_reachable(node, node2, seen):
				return True
		return False

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED!"
    print
