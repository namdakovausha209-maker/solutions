def shortest_distance(kilometers, meters):
    return min(int(kilometers*1000),meters)

if __name__ == "__main__":
    print(shortest_distance(1, 500))
    print(shortest_distance(0.2, 900))
    print(shortest_distance(1,1000))
