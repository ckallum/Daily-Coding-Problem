# Backtracking, if it's valid we carry going down branch following that move, else we prune the branch and try another move


def nQueens(n, board=[]):
    if n == len(board):
        return 1
    count = 0
    for i in range(n):
        board.append(i)
        if isVal(board):
            count += nQueens(n, board)
        board.pop()
    return count


def isVal(board):
    row = len(board) - 1
    col = board[-1]

    for i, j in enumerate(board[:-1]):
        d = abs(col - j)
        if d == 0 or d == row - i:
            return False
    return True


def flightItinerary(tickets, itinerary, start):
    if not tickets:
        return itinerary

    for index, ticket in enumerate(tickets):
        itinerary.append(ticket[0])
        remainingFlights = tickets[:index] + tickets[index+1:]
        if ticket[0] == start:
            if not remainingFlights and ticket[1] != itinerary[0]:
                itinerary.append(ticket[1])
                return itinerary
            else:
                return flightItinerary(remainingFlights, itinerary, ticket[1])
        itinerary.pop()
    return None


def main():
    assert nQueens(0) == 1
    assert nQueens(1) == 1
    assert nQueens(2) == 0
    assert nQueens(3) == 0
    assert nQueens(4) == 2
    trips = [('HNL', 'AKL'), ('YUL', 'ORD'), ('ORD', 'SFO'), ('SFO', 'HNL'), ('AKL', 'YUL')]
    assert flightItinerary(trips, [], 'YUL') == ['YUL', 'ORD', 'SFO', 'HNL', 'AKL']


if __name__ == '__main__':
    main()
