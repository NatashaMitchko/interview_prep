"""
################################################################################
Name of problem: Print Power Set
Problem description: 
    Given an array print the power set of that array. The power set is defined
    to be the set of all subsets of S, including the empty set and S itself.
################################################################################
"""

def print_power_set(arr):
    """This function takes an array and returns an array that is the power set
    of the given array """

    # The power set will always contain the empty set and the set itself
    power_set = [[], arr]

    

"""
################################################################################
First attempt without looking up any answers
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
