"""
         row: (Each row index represents a value from 1 to the goal sum where each
              column represents if the row value can be obtained by using the
               numbers in the number array.
              i.e. 0'th row is initialised as true as we don't need any values from
              the array to achieve a sum of 0
              -> It also lets us set row i as true if a value in the array
                is equal to i as the value of the difference (row - value)
                will equal 0 which is initialised in the
                matrix as true and thus that row will  also be true which is
                correct as we can obtain the value of row i by using a subset of
                a single number equalling to the value of row i.

         col: (Each column index represents the j'th value used in the number array
                where 0 means no values used and 1 means the first value etc.
                The first column is initialised as False as we cannot achieve any
                number>0 by using no numbers in the array)

        Algorithm:
        - The sum of all the numbers must be even to have two equal valued subsets.
            -> k + k = 2k
        - If the sum is even then the two subsets must be equal to half of the total
          -> therefore we evaluate if we can create half of the total using a subset
             of the numbers given. The sum of the numbers not used must be equal to
             the sum of the numbers used to achieve half of the total sum.
        - We work bottom up/row wise(completing a row each iteration), If any of the
          values in the array is equal to the row index then that means the value
          of the row index can be created using the numbers in the array and thus
          that whole row is now true.
          If the current row value is >= than the column index(current number in array)
          then the current row value can be obtained(and thus set to True) if either:
          1. The difference (row value - current number in array) can be created using
            a subset of numbers in the array(i.e subsetarr[difference] == True) and
            thus the value of the current row can be obtained by adding the current
            number to a subset of other numbers in the array.

          2. The row value has already been evaluated as true/obtained by using another
            value /column in the array and thus the whole row is true.

        - We carry this on until we get to the last row representing the sum we want
          to achieve using a subset of numbers in the array
          -> If that row is true this means we can achieve the total sum/2 using some
            subset of the numbers and thus we can create two equal subsets of numbers
            equalling the total sum.
    col : 0 1 2 ......n
        0 T T T.......T
        1 F ...........
        2 F ...........
        . .............
        . .............
   sum//2 F
"""


def can_partition(numbers):
    if sum(numbers) % 2 != 0:
        return None
    else:
        subset_sum = sum(numbers) // 2
        sum_partition = [[True for _ in range(len(numbers) + 1)] for _ in range(subset_sum + 1)]
        for i in range(1, subset_sum + 1):
            sum_partition[i][0] = False

        for i in range(1, subset_sum + 1):
            for j in range(1, len(numbers) + 1):
                sum_partition[i][j] = sum_partition[i][j - 1]
                if i >= numbers[j - 1]:
                    sum_partition[i][j] = sum_partition[i][j] or sum_partition[i - numbers[j - 1]][j - 1]

        return sum_partition[subset_sum][len(numbers)]


def main():
    assert can_partition([15, 5, 20, 10, 35, 15, 10])
    assert not can_partition([15, 5, 20, 10, 35])


if __name__ == '__main__':
    main()
