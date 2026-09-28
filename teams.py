def team_weights(weights):
    first = sum(weights[0::2])   
    second = sum(weights[1::2])
    return (first, second)

