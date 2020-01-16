def find_min(numbers):
    low = 0
    high = len(numbers)-1
    for i in range(4):
        mid = (high+low+1)//2
        print(low, high ,mid)
        if numbers[mid] >= numbers[high]:
            low = mid
        else:
            high = mid
    return numbers[low]


def main():
    assert find_min([5, 7, 10, 3, 4]) == 3


if __name__ == '__main__':
    main()
