def next_spare_number(number):
    num_bin = str(bin(number))[2:]
    num_bin = list(reversed(num_bin))
    num_bin.append("0")
    prev_index = 0
    for i in range(1, len(num_bin)-1):
        if num_bin[i] == "1" and num_bin[i - 1] == "1" and num_bin[i + 1] != "1":
            num_bin[i + 1] = "1"
            for j in range(i, prev_index - 1, -1):
                num_bin[j] = "0"
            prev_index = i + 1


    return int("".join(num_bin[::-1]), base=2)


def main():
    assert next_spare_number(0) == 0
    assert next_spare_number(1) == 1
    assert next_spare_number(2) == 2
    assert next_spare_number(3) == 4


if __name__ == '__main__':
    main()

"""
0 -> 1
1 -> 10
10 -> 100
11 -> 101
"""
