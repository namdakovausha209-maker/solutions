import sys
import math
def tetration(x, n):
    if n == 0:
        return 1 
    else:
        return x ** tetration(x, n - 1)

if __name__ == "__main__":
    sys.set_int_max_str_digits(100000)
    print(tetration(2, 0))
    print(tetration(5, 2))
    
