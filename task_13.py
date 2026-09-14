def multiplication_table(n):
    result = []
    for i in range(1, 11):
        result.append(f"{n} x {i} = {n * i}")
    return result
