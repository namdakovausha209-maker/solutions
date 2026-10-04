def factorial(n):
    result = 1
    if n <0:
        return None
    if n == 0:
        return 1
    else:
        for i in range(2, n+1):
            result *= i
    return result

def arrangements(n, k):
    resultN = 1
    resultK = 1
    if n < 0 or k < 0:
        return None
    if n > k:
        for i in range(2, n+1):
            resultN *= i
        for i in range(2, (n-k)+1):
            resultK *= i
        A = resultN / resultK
        return A
    else:
        return 0

def combinations(n, k):
    resultN = 1
    resultK = 1
    resultNK = 1
    if n < 0 or k < 0:
        return None
    if n > k:
        for i in range(2, n+1):
            resultN *= i
        for i in range(2, (n-k)+1):
            resultNK *= i
        for i in range(2, k+1):
            resultK *= i
        A = resultN / (resultK * resultNK)
        return A
    else:
        return 0
