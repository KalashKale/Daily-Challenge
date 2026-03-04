def blood_moon(time):
    hours = int(time[0:2])
    minutes = int(time[3:5])

    total_minutes = hours * 60 + minutes

    result = []
    interval = 168  # 2 hours 48 minutes, as given
    day_hours = 1440  #24 hours
    for _ in range(3):
        total_minutes = (total_minutes + interval) % day_hours
        
        new_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        
        result.append(f"{new_hours:02}:{new_minutes:02}")

    return result