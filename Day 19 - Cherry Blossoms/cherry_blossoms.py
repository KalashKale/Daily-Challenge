def cherry_blossoms(temps):
    # Write code below 💖
    for i in range(4, len(temps)):
        window_avg = sum(temps[i-4:i+1]) / 5
        
        if window_avg > 15:
            return i + 1
    
    return -1

print(cherry_blossoms([10, 11, 13, 14, 16, 17, 18]))