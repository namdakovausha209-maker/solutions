def pasture_area(wire, w):
    area = (wire*w - 2*w**2)/3
    return area
def best_pasture(wire):
    w = wire/4
    l = (100 - 2*w)/3
    area  = (wire*w - 2*w**2)/3
    return (w, l ,area)

def best_pasture_bruteforce(wire):
    step = 0.001
    best_w = 0
    best_area = 0
    w = 0
    while w <= wire/2:
        area = (wire*w - 2*w**2)/3
        if area > best_area:
            best_area = area
            best_w = w
        w+=step
    l = (100 - 2*best_w)/3
    return (best_w, l, best_area)

if __name__ == "__main__":
    print(pasture_area(100, 25))     # 416.666...
    print(pasture_area(100, 10))     # 266.666...
    print(pasture_area(100, 50))     # 0.0    вся проволока ушла на ширину

    print(best_pasture(100))         # (25.0, 16.666..., 416.666...)
    print(best_pasture(60))          # (15.0, 10.0, 150.0)
    print(best_pasture(12))          # (3.0, 2.0, 6.0)

    