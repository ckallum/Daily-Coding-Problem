"""

Timetabling problem solving -> sort all times,
if there is no end time in-between start times number of
classrooms needed increases. Once there is an end time we
can subtract the number of extra rooms needed as a class has ended
and we don't need that room. If there is another start time we can reuse
that previously subtracted room

"""


def findCount(times):
    sortedTimes = []
    for interval in times:
        sortedTimes.append((interval[0], 'start'))
        sortedTimes.append((interval[1], 'end'))

    maxRooms = 0
    currentRooms = 0
    for time, key in sorted(sortedTimes):
        if key == 'start':
            currentRooms += 1
        else:
            currentRooms -= 1
        if currentRooms > maxRooms:
            maxRooms = currentRooms

    return maxRooms


def main():
    times = [(30, 75), (0, 50), (60, 150)]
    assert findCount(times) == 2


if __name__ == '__main__':
    main()
