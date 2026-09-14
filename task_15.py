def days_in_month(month, year):
    dim = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and year % 4 == 0 and year % 100 != 0:
        return 29
    return dim[month]

