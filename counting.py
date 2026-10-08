def factorial(n):
    if n < 0: return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def arrangements(n, k):
    if k > n or n < 0 or k < 0: return 0
    return factorial(n) / factorial(n - k) # pyright: ignore

def combinations(n, k):
    if k > n or n < 0 or k < 0: return 0
    return arrangements(n, k) / factorial(k) # pyright: ignore
