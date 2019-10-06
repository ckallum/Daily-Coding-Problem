from cmath import inf


def is_prime(i, j):
    i_count = 0
    for x in range(1, i // 2):
        if i % x == 0:
            i_count += 1
        if i_count > 1:
            return False

    j_count = 0
    for x in range(1, j // 2):
        if j % x == 0:
            j_count += 1
        if j_count > 1:
            return False
    return True


def find_primes(number):
    solution = (inf, inf)
    for i in range(2, int(number / 2) + 1):
        num1 = i
        num2 = number - i
        possible = is_prime(num1, num2)
        if possible:
            if num1 < solution[0]:
                solution = (num1, num2)
            elif num1 == solution[0] and num2 < solution[1]:
                solution = (num1, num2)

    return solution


def main():
    assert find_primes(4) == (2, 2)
    assert find_primes(8) == (3, 5)


if __name__ == '__main__':
    main()