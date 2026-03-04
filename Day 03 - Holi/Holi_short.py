def find_missing_colors(grid):
    all_colors = {"🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"}
    
    found = {color for row in grid for color in row}
    
    return [color for color in ["🟥","🟧","🟨","🟩","🟦","🟪","🟫"] if color not in found]