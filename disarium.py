def is_disarium(num):
    s = str(num)
    result = 0
    for pos, digit in enumerate(s, start=1):
        result += int(digit) ** pos
    return result == num

