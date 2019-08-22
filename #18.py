from collections import deque


def findMaxes(arr, subsSize):
    res = list()
    if not arr:
        return None

    if len(arr) <= subsSize:
        return list(max(arr))

    for index, val in enumerate(arr[:-subsSize + 1]):
        sub = arr[index:index + subsSize]
        res.append(max(sub))
    return res


def windowSlidingMax(arr, subSize):
    if not arr:
        return None

    if len(arr) <= subSize:
        return list(max(arr))

    res = list()
    dq = deque()

    for i in range(subSize):
        while dq and arr[i] > arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    res.append(arr[dq[0]])

    for i in range(subSize, len(arr)):
        while dq and dq[0] <= i - subSize:
            dq.popleft()

        while dq and arr[i] > arr[dq[-1]]:
            dq.pop()
        dq.append(i)
        res.append(arr[dq[0]])
    return res


def main():
    arr = [10, 5, 2, 7, 8, 7]
    assert findMaxes(arr, 3) == [10, 7, 8, 8]
    assert windowSlidingMax(arr, 3) == [10, 7, 8, 8]


if __name__ == '__main__':
    main()
