from random import random
import bisect


def get_new_state(current_state, transitions):
    transition_map = dict()
    for source, target, probability in transitions:
        if source not in transition_map:
            transition_map[source] = ([], [])
        if not transition_map[source][0]:
            transition_map[source][0].append(probability)
        else:
            prev = transition_map[source][0][-1]
            transition_map[source][0].append(probability + prev)
        transition_map[source][1].append(target)
    r = random()
    index = bisect.bisect(transition_map[current_state][0], r)
    print(transition_map)
    return transition_map[current_state][1][index]


def markov(start, transitions):
    current_state = start
    states = dict()
    for t in transitions:
        states[t[0]] = 0
    for i in range(5000):
        states[current_state] += 1
        current_state = get_new_state(current_state, transitions)
    return states


def main():
    visited = (markov('a', [
        ('a', 'a', 0.9),
        ('a', 'b', 0.075),
        ('a', 'c', 0.025),
        ('b', 'a', 0.15),
        ('b', 'b', 0.8),
        ('b', 'c', 0.05),
        ('c', 'a', 0.25),
        ('c', 'b', 0.25),
        ('c', 'c', 0.5)
    ]))
    assert visited['a'] > visited['b']
    assert visited['a'] > visited['c']
    assert visited['b'] > visited['c']


if __name__ == '__main__':
    main()
