"""
################################################################################
Name of problem: How long is the longest sentence in the given text?
Problem description: 
    Write a function that takes a text file as a parameter and 
    counts the words in each sentence. The function should return an integer that 
    represents the number of words in the longest sentence. Sentences will only
    be seperated by periods, question marks or exclamation points (., !, ?) and
    words must have letters in them ('2' is not a word).
################################################################################
"""



"""
################################################################################
First attempt without looking up any answers
################################################################################
"""
import re


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
