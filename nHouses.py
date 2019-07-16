from random import randrange
import sys


def findMin(costMatrix, houses, colours):
    prevMin = 0
    prevMinIndex = -1
    prevAltMin = 0
    for j in range(houses):
        currentMin = sys.maxsize
        currentAltMin = sys.maxsize
        currentMinIndex = -1
        for i in range(colours):
            if i == prevMinIndex:
                costMatrix[j][i] += prevAltMin
            else:
                costMatrix[j][i] += prevMin
            if costMatrix[j][i] < currentMin:
                currentAltMin = currentMin
                currentMin = costMatrix[j][i]
                currentMinIndex = i
            elif costMatrix[j][i] < currentAltMin:
                currentAltMin = costMatrix[j][i]
        prevMin = currentMin
        prevAltMin = currentAltMin
        prevMinIndex = currentMinIndex
    return min(costMatrix[houses-1])


def main():
    colours = 5
    houses = 6
    matrix = [[randrange(100) for _ in range(colours)] for _ in range(houses)]
    for row in range(len(matrix)):
        print(matrix[row], end ='\n')
    print(findMin(matrix, houses, colours))


if __name__ == '__main__':
    main()