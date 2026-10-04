def bytes_to_kilobytes(value):
    a = value / 1024
    return a

def kilobytes_to_bytes(value):
    a = value * 1024
    return a

if __name__ == "__main__":
    bytes_to_kilobytes(2048)
    kilobytes_to_bytes(2)
