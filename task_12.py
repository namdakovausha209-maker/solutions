def shortest_distance(kilometers, meters):
    if kilometers * 1000 > meters:
        return meters
    elif kilometers * 1000 == meters:
        return meters
    else:
        return kilometers * 1000

