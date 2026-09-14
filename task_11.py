def guests_by_seat(seats):
    guests = [None] * max(seats)
    for i in range(len(seats)):
        guests[seats[i] - 1] = i + 1
    return guests

