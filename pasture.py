def pasture_area(wire, w):
    return (wire - 2 * w) / 3 * w

def best_pasture(wire):
    w = wire / 4
    A = pasture_area(wire, w)
    l = A / w
    return (w, l, A)

def best_pasture_bruteforce(wire):
    best_w = 0
    best_l = 0
    best_A = 0
    for w in range(1, wire):
        A = pasture_area(wire, w)
        l = A / w
        if A > best_A:
            best_w = w
            best_l = l
            best_A = A
    return (best_w, best_l, best_A)

    
