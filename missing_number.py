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

"""
################################################################################
Solution inspired by looking at the solution(s) of others:

    This problem can get more complicated by asking "what if there are two
    missing numbers?" and also "what if there are k missing numbers?"
################################################################################
"""
import numpy

def two_missing(lst, max):
    """Returns the two missing numbers from the sequence using a sum and sum of
    squares method
        
        >>> two_missing([1,3,5], 5)
        (2, 4)
    """
    sum_of_items = (max * (max + 1)) / 2 - sum(lst)
    sum_of_squares = (max * (max + 1) * (2 * max + 1)) / 6 - sum([i^2 for i in lst])
    
    # (sum_of_items - missing1)^2 + missing1^2 = sum_of_squares
    # 2*missing^2 + 2*sum_of_items*missing - sum_of_squares = 0
    # Solve for roots using numpy

    return [2*sum_of_items, -(sum_of_squares)]
  
    




if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED!"
    print
