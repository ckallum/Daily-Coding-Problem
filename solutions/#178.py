from random import randint


### https://www.reddit.com/r/slatestarcodex/comments/73nvur/a_dead_simple_probability_puzzle_that_you_will/


def roll_dice(game, index):
    rand = randint(1, 6)
    if game[index] == rand:
        index += 1
    elif game == [5, 6]:
        if not (index == 1 and rand == 5):
            if index > 0:
                index -= 1
    else:
        if index > 0:
            index -= 1
    if index == len(game):
        return 1

    return 1 + roll_dice(game, index)


def simulate_game(game):
    penalty = roll_dice(game, 0)
    return penalty


def main():
    experiments = 10000
    games = [[5, 6], [5, 5]]
    i = 0
    averages = [0, 0]
    for game in games:
        pen = 0
        for _ in range(experiments):
            pen += simulate_game(game)
        avg = pen / experiments
        averages[i] = round(avg)
        i += 1
    print(averages)
    assert averages == [36, 42]

if __name__ == '__main__':
    main()
