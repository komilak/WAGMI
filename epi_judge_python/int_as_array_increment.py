from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # add each int col by col
    # first, add 1 to the single digit val

    # then, from singles upwards (right to left) check if we have to carry over any digits
    for i in reversed(range(0, len(A))):
        A[i] += 1
        # if the digit doesn't have overflow
        # then there is no need to do anything else
        # and we can just return the resulting array
        if A[i] != 10:
            break
        # else, we need update the val of the single digit to just 0 and carry the 1
        # to the prev (1 to the left) val
        elif A[i] == A[0]:
            A.append(0)
            A[0] = 1
        # if the digit we're on is now 10 or greater, set to 0
        # and continue the loop to carry the one
        else:
            A[i] = 0

    # check the leftmost val - we can only hold a single digit
    # so if there's a 1 to carry, we need to add a 0 to the end of the total #
    # and update leftmost to a new 1 _ths val
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
