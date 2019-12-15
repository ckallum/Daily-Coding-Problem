# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# You are given a list of data entries that represent entries and exits
# of groups of people into a building. An entry looks like this:
#
# {"timestamp": 1526579928, count: 3, "type": "enter"}
#
# This means 3 people entered the building. An exit looks like this:
#
# {"timestamp": 1526580382, count: 2, "type": "exit"}
# Find the busiest period in the building, that is, the time with the most
# people in the building. Return it as a pair of (start, end) timestamps.
# You can assume the building always starts off and ends up empty,
# i.e. with 0 people inside.
from cmath import inf


def get_busiest_slot(events):
    entries, exits = dict(), dict()
    min_time = inf
    max_time = -inf
    for event in events:
        if event["type"] == "enter":
            entries[event["timestamp"]] = event["count"]
        else:
            exits[event["timestamp"]] = event["count"]
        if event["timestamp"] < min_time:
            min_time = event["timestamp"]
        if event["timestamp"] > max_time:
            max_time = event["timestamp"]
    max_count, count = -inf, 0
    start, end = None, None
    for time in range(min_time, max_time + 1):
        if time in entries:
            count += entries[time]
            if count > max_count:
                max_count = count
                start = time
        elif time in exits:
            count -= exits[time]
            if count == 0:
                end = time

    return start, end


def main():
    events = [
        {"timestamp": 1526579928, "count": 3, "type": "enter"},
        {"timestamp": 1526579982, "count": 4, "type": "enter"},
        {"timestamp": 1526580054, "count": 5, "type": "exit"},
        {"timestamp": 1526580128, "count": 1, "type": "enter"},
        {"timestamp": 1526580382, "count": 3, "type": "exit"}
    ]
    assert get_busiest_slot(events) == (1526579982, 1526580054)


if __name__ == '__main__':
    main()
