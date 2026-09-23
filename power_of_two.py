import math

def is_power_of_two(n):
    if n <= 0:
        return False
    log_result = math.log2(n)
    return log_result == int(log_result)

