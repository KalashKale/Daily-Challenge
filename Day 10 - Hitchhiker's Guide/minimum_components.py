def minimum_components(components):
  # Write code below 💖
    target = 42
    best = float('inf')

    def dfs(i, current_sum, count):
        nonlocal best

        if current_sum == target:
            best = min(best, count)
            return
        
        if current_sum > target or i == len(components) or count >= best:
            return

        # take this number
        dfs(i + 1, current_sum + components[i], count + 1)

        # skip this number
        dfs(i + 1, current_sum, count)

    dfs(0, 0, 0)

    return best if best != float('inf') else -1
