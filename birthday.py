def birthday_probability(people):
    days = 365
    result = 1
    for i in range((days - people)+1, days):
        result *= i/365 
    return 1 - result

# import random

# def estimate_empty_team(candidates, trials=100_000):
#     """Доля экспериментов, где не взяли ни одного кандидата."""
#     hits = 0
#     for _ in range(trials):
#         coins = [random.choice(["орёл", "решка"]) for _ in range(candidates)]
#         if all(coin == "решка" for coin in coins):
#             hits += 1
#     return hits / trials

# print(estimate_empty_team(4))    # около 0.0625, то есть 1/16
# print(estimate_empty_team(23))   # почти наверняка 0.0

import random
def simulate_birthday(people, trials):
    hits = 0
    for _ in range(trials):
        birthdays = [random.randint(1,365) for _ in range(people)]
        if len(set(birthdays)) < len(birthdays):
            hits += 1
    return hits/trials

print(simulate_birthday(23,10000))