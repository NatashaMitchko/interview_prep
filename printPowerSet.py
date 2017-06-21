"""
################################################################################

Name of problem: Print Power Set
Problem description: 
    Given an array print the power set of that array. The power set is defined
    to be the set of all subsets of S, including the empty set and S itself.

################################################################################
"""
"""
################################################################################
First attempt without looking up any answers
################################################################################
"""


def print_power_set(arr):
    """This function takes an array and returns an array that is the power set
    of the given array. This solution assumes that there are no duplicate items
    in the set. 

        >>> print_power_set([1, 2, 3])
        [[], [1, 2, 3], [1], [2], [3], [1, 2], [1, 3] [2, 3]]

    """

    # The power set will always contain the empty set and the set itself
    power_set = [[], arr]

    # The power set also contains the set of every individual element
    for item in arr:
        power_set.append([item])

    # The power set also contains the set of the doubles
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            power_set.append([arr[i], arr[i+1]])

    print power_set




    


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
