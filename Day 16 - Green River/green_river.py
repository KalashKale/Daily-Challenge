def lucky_river(river, hours):
  # Write code below 💖
    n = len(river)

    for _ in range(hours):
        new_river = river[:]   # making copy of the list

        for i in range(n - 1):
            if river[i] == '☘️':
                new_river[i + 1] = '☘️'

        river = new_river

    return river