def sum_interval(a, b):
    l = min(a, b)
    r = max(a, b)
    n = r - l + 1
    total = n * (l + r) // 2
    return total

print(sum_interval(1, 2))