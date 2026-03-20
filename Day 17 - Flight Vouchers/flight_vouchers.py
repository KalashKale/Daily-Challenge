def pick_voucher(vouchers, delays, max_wait):
  # Write code below 💖
    best_ratio = -1
    best_index = -1

    for i in range(len(vouchers)):
        if delays[i] <= max_wait:
            ratio = vouchers[i] / delays[i]

            if ratio > best_ratio:
                best_ratio = ratio
                best_index = i

    return best_index

print(pick_voucher([50, 120, 20],[2, 4, 1],3))