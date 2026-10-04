from math import factorial
def is_strong(n):
    numbers = str(n)
    sum_of_factorials = sum(factorial(int(i)) for i in numbers)
    return sum_of_factorials == n

if __name__ == "__main__":
    for i in range(1, 100000):
        if is_strong(i):
            print(f"Найдено сильное число: {i}")
