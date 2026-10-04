def swap(a,b):
    a = a * b
    b = a // b
    a = a // b
    return (a,b)

if __name__ == "__main__":
    print(swap(5,2))
