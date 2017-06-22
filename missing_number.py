"""
################################################################################
Name of problem: Missing Number
Problem description: Given a list containing the integers from 1 to a max number,
find the number that's missing from that sequence. The function should take a 
list and the max number in the list and return the missing number.
################################################################################
"""
"""
################################################################################
First attempt without looking up any answers
################################################################################
"""

def missing_number(lst, max):
    """
    See notes below. Runtime is O(n)

        >>> missing_number([1,2,3,5], 5)
        4
        >>> missing_number([2,3], 3)
        1
        >>> missing_number([1,2], 3)
        3
    """
    return (max*(max+1))/2 - sum(lst)

"""
################################################################################
Notes:

    I suprised myself on this one by getting an answer in one line that had a 
    reasonable runtime. This solution exploits the fact that sequences of numbers
    can be represented as serries (a sum of all the numbers in the sequence)
    and that often those series have a general solution. In this case the
    serries 1 + 2 + 3 + ... + n is an algrbraic serries that evaluates to 
    (n(n+1))/2. To find the missing number you find the sum of the sequence
    without any missing numbers and subtract the sum of the items in the given 
    list. The result will be the missing number.
    
################################################################################
"""

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED!"
    print
