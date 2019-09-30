"""
    To get the next possible number in lexicographic order means getting the next
    number that is bigger than the current number using the numbers provided.
    AKA get the number that is bigger than the current number where the difference
    between the two numbers is the smallest possible.

    Traverse numbers in reverse order, as the next largest number in lexicographic order
    will change from the smallest digits in the number first, if there is a change possible at all.

    This means we want to change the biggest digits in the number
    as little as possible and focus on changing the lower value digits/tail end of the number.


    We find the first index, where the number at that digit is larger than the number in the next digit after it. This
    means all numbers before the current index are in descending order, where the last element
    is currently the smallest element in the tail end(subarray) of the array.

         - We stop at this index as we have found the digit in the number we need to increase(index -1) to get the next
           number in lexicographic order. We use this digit as the invariant states all digits before are in descending
           order and swapping any of those digits will result in making the number smaller which wouldn't be the next
           number in lexicographic order. Basically, we are finding the next digit position we know we can increase by
           using the numbers we have already traversed.

         - We then find the next smallest number and swap it's position with this smallest number at index-1
           by traversing the tail subarray we have already evaluated in reverse which finds the first number
           that is larger than the current smallest in the tail.

         - By swapping these two numbers and then reversing the tail portion(which by invariant is still
           in descending order) means we are increasing the number and by reversing the tail it changes to ascending
           order aka the smallest number possible->we get the next increment of the number in lexicographic order.

"""


def next_lexicographic_number(numbers):
    index = len(numbers)-1
    while index > 0:
        if index > 0 and numbers[index] > numbers[index - 1]:
            break
        index -= 1

    if index == 0:
        numbers.reverse()
    else:
        for i in range(len(numbers) - 1, index - 1, -1):
            if numbers[i] > numbers[index - 1]:
                temp = numbers[i]
                numbers[i] = numbers[index - 1]
                numbers[index - 1] = temp
                break

        tail = numbers[index:]
        tail.reverse()
        numbers[index:] = tail

    return numbers


def main():
    assert next_lexicographic_number([1, 2, 3]) == [1, 3, 2]
    assert next_lexicographic_number([1, 3, 2]) == [2, 1, 3]
    assert next_lexicographic_number([3, 2, 1]) == [1, 2, 3]


if __name__ == '__main__':
    main()
