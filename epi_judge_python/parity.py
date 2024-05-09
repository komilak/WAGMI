from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    result = 0

    # while the number is not yet reduced to 0
    # loop is skipped if num is 0, parity is 0 by default
    # while x:
    #     result ^= 1
    #     # x&(x-1) is x with its lowest bit erased
    #     x &= x - 1
    #
    # return result
    #
    # improvement:
    #
    # The XOR of two bits = 0 if both bits are 0 or 1
    # The XOR of a group of bits is its parity
    # continue XORing half of the bitset over and over to get total parity
    # parity of 64 bit = 2 32 bit = 4 16 bit, etc
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1



if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
