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

    width = 1

    for i in range(len(a)-width):
        for j in range(len(a)-width):
            print a[i:i+width] + [a[j+width]]

    print power_set

def print_power_set_recursive(arr, width=0, power_set=[]):
    """Recursive solution to print power set.

        >>> print_power_set_recursive([1, 2, 3])
        [[], [1], [2], [3], [1, 2], [1, 3] [2, 3], [1, 2, 3]]

    """

    if width + 1 == len(arr):
        power_set.append(arr)
        print power_set
        return
    if width == 0:
        power_set.append([])
    elif width == 1:
        for item in arr:
            power_set.append([item])
    else:
        for i in range(len(arr) - width):
            for j in range(len(arr) - width):
                power_set.append(arr[i:i+width] + [arr[j+width]])

    # recursive call here
    print_power_set_recursive(arr, width+1, power_set)

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
