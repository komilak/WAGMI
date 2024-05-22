from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # # take in one at a time
    # isNeg = False
    #
    # # Check if the integer is negative, set a boolean accordingly,
    # # and set the integer to positive if needed
    # if x < 0 :
    #     x = -x
    #     isNeg = True
    #
    # # Iterate through the number, and add each digit to the end of a list
    # # prepending is expensive for arrs/strings so wait to reverse at the end
    #
    # # chr(i) returns a string of one character whose ASCII code is the integer i
    # # ord('a') returns an integer representing the ASCII code of the character
    # # chr(i) and ord('a') are the inverse of each other
    # newStr = []
    # while True:
    #     # extract last digit
    #     newStr.append((chr(ord('0') + x % 10)))
    #     # div by 10 to cut down the int, get next last dig in place
    #     x //= 10
    #     if x == 0:
    #         break
    #
    # # return a neg at beg if int is neg,
    # # then add the reversed string (now correct order) to output
    # # init an arr for reversal, add to empty '' to stringify
    # return ('-' if isNeg else '') + ''.join(newStr[::-1])
    is_negative = False
    if x < 0:
        x = -x
        is_negative = True

    s = []
    while True:
        s.append((chr(ord('0') + x % 10)))
        x //= 10
        if x == 0:
            break
    return ('-' if is_negative else '') + ''.join(s[::-1])


def string_to_int(s: str) -> int:
    is_neg = False
    # if there is a neg sign, just flag it and
    # adjust the pointer to where the nums start
    if s[0] == '-':
        s = s[1:]
        is_neg = True

    result = 0
    # with each increase in the 10's, mult prev result by 10 accordingly
    # then add on the intified num
    for i in range(len(s)):
        result = result * 10 + (ord(s[i]) - ord('0'))

    return -result if is_neg else result



def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
