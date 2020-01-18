"""
Goal is to find the first available unit's digit that can be replaced by a units digit lower than it -> i.e. smallest
possible increase in number = next lexographic permutation
We then find the next largest number in the previous digits to replace -> swap the numbers.
We then reverse the number from the replaced units index+1 of the number(i.e. reverse the tail)
    Currently the tail is guaranteed to be in descending order -> reversing the tail is the smallest increase possible
    as  we have already guaranteed a larger number by swapping the identified unit->goal is to find smallest possible
    increase.
        i.e 6215430 -> swap 1 and 3-> 6235410 ->reverse from swapped index onward(reverse 0145)-> 6230145
"""


def next_lexographic_permutation(number):
    number = list(str(number))
    i = 0
    replaced = None
    for i in range(len(number) - 2, 0, -1):
        if number[i] < number[i + 1]:
            replaced = number[i]
            break
    for j in range(len(number) - 1, i, -1):
        if number[j] > replaced:
            number[i], number[j] = number[j], number[i]
            break
    number[i + 1:] = reversed(number[i + 1:])
    return int("".join(number))


def main():
    assert next_lexographic_permutation(48975) == 49578


if __name__ == '__main__':
    main()
