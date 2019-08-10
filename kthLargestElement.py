# MinHeap or max heap data structure
import heapq


def find(numbers, k):
    numbers.sort()
    return numbers[-k]


def maxHeapSolution(numbers, k):
    return heapq.nlargest(3, numbers)[k-1]


def main():
    assert find([3, 5, 2, 4, 6, 8], 3) == 5
    assert maxHeapSolution([3, 5, 2, 4, 6, 8], 3) == 5


if __name__ == '__main__':
    main()
