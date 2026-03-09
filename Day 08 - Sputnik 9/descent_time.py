def calculate_descent(altitude):
    # Write code below 💖
    layers = [
        (700, 10000, 2000),
        (85, 700, 500),
        (50, 85, 200),
        (12, 50, 75),
        (0, 12, 20)     
    ]

    time = 0.0

    for low, high, rate in layers:
        if altitude > low:
            top = min(altitude, high)
            distance_km = top - low
            time += (distance_km * 1000) / rate
            altitude = low

    return round(time, 1)