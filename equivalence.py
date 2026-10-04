from itertools import product

def are_equivalent(f, g, n):
    for row in product([True, False], repeat=n):
        if f(*row) != g(*row):
            return False
    return True

def de_morgan_left(a, b):
    return not (a and b)

def de_morgan_right(a, b):
    return (not a) or (not b)

def wrong(a, b):
    return (not a) and (not b)

if __name__ == "__main__":
    print(are_equivalent(de_morgan_left, de_morgan_right, 2))   # True
    print(are_equivalent(de_morgan_left, wrong, 2))