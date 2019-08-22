"""
If there is 3 occurrences of a number, by converting the number to binary, the addition of each i'th bit of the number
mod 3 should = 0 i.e 5 = 101, therefore doing this i'th bit modular addition over all the values where there is 3
of each value should equate to 0.
If there is a value where there isn't 3 occurrences of it(the result), then we know that the result of adding all
the i'th bits mod3 will be the i'th bit of the value with one occurrence as the addition of the rest of
the bits are guaranteed to result in 0 mod3 as there would be multiple of 3 occurrences of the same bit
across those values.

i.e [ 5, 5, 5, 8] == [101, 101, 101, 1000]
0  1  0  1
0  1  0  1
0  1  0  1
1  0  0  0
-----------
1  0  0  0  = 8

"""


def find(arr):
    non_duplicate = 0

    for i in range(0, 32):  # O(32n) = word size
        sum_i_position_bits = 0
        x = 1 << i  # Checking i'th bit of each number
        for j in range(len(arr)):
            if arr[j] & x:  # Bit wise and to check if the bit i of value at arr[j] = 1
                sum_i_position_bits += 1

        if sum_i_position_bits % 3:  # If there is a remainder
            non_duplicate = non_duplicate | x

    return non_duplicate


def main():
    assert find([6, 1, 3, 3, 3, 6, 6]) == 1
    assert find([13, 19, 13, 13]) == 19


if __name__ == '__main__':
    main()
