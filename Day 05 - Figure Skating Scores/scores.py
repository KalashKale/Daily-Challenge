def calculate_score(elements):
  
  total_score = 0

  for name, base, goe in elements:
    trimmed = sorted(goe)[1:-1]
    avg_goe = sum(trimmed) / len(trimmed)
    element_score = base + (avg_goe * 0.1 * base)
    total_score += element_score

  return round(total_score, 1)