def guests_by_seat(seats):
    guests = [None] * max(seats)
    for i in range(len(seats)):
        guests[seats[i] - 1] = i + 1
    return guests

if __name__ == "__main__":
    print(guests_by_seat([1, 2, 3, 5, 4]))
    print(guests_by_seat([11, 6, 8, 2, 10, 9, 4, 7, 3, 1, 5]))
