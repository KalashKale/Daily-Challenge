def analyze(percentages):
    # Write code below 💖
    net_change_annual = round((percentages[-1] - percentages[0]) / (len(percentages) - 1), 4)

    first_sum = 0
    for i in range(3):
        first_sum += percentages[i]
    
    first_three_average = first_sum / 3
    
    last_three_average = sum(percentages[-3:]) / 3

    if (first_three_average < last_three_average):
        trend = "improving"
    elif (first_three_average == last_three_average):
        trend = "stagnating"
    elif (first_three_average > last_three_average):
        trend = "declining"
    
    dips = 0
    for i in range(len(percentages) - 1):
        if(percentages[i] > percentages[i+1]):
            dips += 1

    return net_change_annual, trend, dips