def truth_table(n):
    if n == 0:
        return [()]  
    prev_table = truth_table(n - 1)
    result = []
    for row in prev_table:
        result.append(row + (0,))  
        result.append(row + (1,))
    return result
