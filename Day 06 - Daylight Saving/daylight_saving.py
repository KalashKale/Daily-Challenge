def calculate_sleep_debt(planned, actual):
  # Write code below 💖
    total_debt = 0
    current_streak = 0
    max_streak = 0

    for i in range(len(planned)):
        debt = max(0, planned[i] - actual[i])
        total_debt += debt

        if debt > 0:
            current_streak += 1
        else:
            current_streak = 0

        max_streak = max(max_streak, current_streak)

    total_debt += 1

    return total_debt, max_streak