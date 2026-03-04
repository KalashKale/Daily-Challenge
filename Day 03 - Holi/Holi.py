def find_missing_colors(grid):
    all_colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
    
    colors_found = set()
    
    for row in grid:
        for color in row:
            colors_found.add(color)
    
    missing = []
    
    for color in all_colors:
        if color not in colors_found:
            missing.append(color)
    
    return missing