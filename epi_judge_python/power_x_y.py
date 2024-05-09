from test_framework import generic_test


def power(x: float, y: int) -> float:
    # x to the power of y
    # When y is a power of 2, the multiplications can be iterated by squaring like x, x 2, (x 2 ) 2
    # When y is nonnegative, if the least significant bit of y is 0, the result is (x y ∕ 2 ) 2
    # When y is nonnegative, if the least significant bit of y is 1, the result is x × (x y ∕ 2 ) 2
    # When y is negative, if the least significant bit of y is 0, the result is (1 ∕ x -y ∕ 2 ) 2
    # When y is negative, if the least significant bit of y is 1, the result is 1 ∕ x × (1 ∕ x -y ∕ 2 ) 2
    result = 1
    if y < 0:
        y = -y
        x = 1/x
    # loop until y/power = 0
    while y:
        # If the least sig bit of y is 1, compute the result = result × x
        if y & 1:
            result *= x
        # Compute x = x × x and y = y ∕ 2
        x *= x
        y >>= 1

    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
