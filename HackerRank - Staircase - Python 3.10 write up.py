##    Staircase detail
##
##    This is a staircase of size n = 4:
##
##       #
##      ##
##     ###
##    ####
##
##    Its base and height are both equal to n. It is drawn using # symbols and
##    spaces. The last line is not preceded by any spaces.
##
##    Write a program that prints a staircase of size n. 

##### ##### ##### #####

#   Iterative solution
#   O(n): n is an integer
#   Key Concepts:
#       How the addition and multiplication symbol interact with strings.

def solutionOne(n):

    for i in range(1, n+1):

        print((' ' * (n-i)) + ('#' * i))

    return None

##### ##### ##### #####

def test():

    border = '##### ##### ##### #####'
    successful_test = 'All tests completed successfully.'

    test_case_one = 4

    print()
    print(border)
    print()

    solutionOne(test_case_one)

    print()
    print(border)
    print()

    return successful_test
