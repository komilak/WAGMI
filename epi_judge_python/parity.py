from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    result = 0

    # while the number is not yet reduced to 0
    # loop is skipped if num is 0, parity is 0 by default
    while x:
        result ^= 1
        # x&(x-1) is x with its lowest bit erased
        x &= x - 1
        
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
