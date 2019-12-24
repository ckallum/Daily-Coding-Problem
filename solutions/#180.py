"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
"""
from queue import Queue


def interleave_reverse(stack, queue, index=1):
    for i in range(len(stack) - index):
        queue.put(stack.pop())
    while queue.qsize():
        stack.append(queue.get())
    print(stack)
    if len(stack) - index > 1:
        stack = interleave_reverse(stack, queue, index + 1)

    return stack


def main():
    queue = Queue()
    assert interleave_reverse([1, 2, 3, 4, 5], queue) == [1, 5, 2, 4, 3]
    queue = Queue()
    assert interleave_reverse([1, 2, 3, 4], queue) == [1, 4, 2, 3]


if __name__ == '__main__':
    main()
