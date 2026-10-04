def is_tidy(n):
    s = str(n)
    return s == ''.join(sorted(s))

if __name__ == "__main__":
    print(is_tidy(12))      # True
    print(is_tidy(32))      # False
    print(is_tidy(13579))   # True
    print(is_tidy(2335))    # True
    print(is_tidy(7))       # True
