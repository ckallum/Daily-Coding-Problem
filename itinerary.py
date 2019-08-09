# Backtracking, if it's valid we carry going down branch following that move, else we prune the branch and try another move


def flightItinerary(tickets, itinerary, start):
    if not tickets:
        return itinerary

    for index, ticket in enumerate(tickets):
        itinerary.append(ticket[0])
        remainingFlights = tickets[:index] + tickets[index + 1:]
        if ticket[0] == start:
            if not remainingFlights and ticket[1] != itinerary[0]:
                itinerary.append(ticket[1])
                return itinerary
            else:
                return flightItinerary(remainingFlights, itinerary, ticket[1])
        itinerary.pop()
    return None


def main():
    trips = [('HNL', 'AKL'), ('YUL', 'ORD'), ('ORD', 'SFO'), ('SFO', 'HNL'), ('AKL', 'YUL')]
    assert flightItinerary(trips, [], 'YUL') == ['YUL', 'ORD', 'SFO', 'HNL', 'AKL']
    assert flightItinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], [], 'A') == ['A', 'B', 'C', 'A', 'C']


if __name__ == '__main__':
    main()

