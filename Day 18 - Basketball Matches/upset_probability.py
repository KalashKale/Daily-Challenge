def upset_probability(matchups):
  # Write code below 💖
    result = []

    for game in matchups:
        seedA = game[1]
        seedB = game[3]

        prob = seedA / (seedA + seedB)
        result.append(round(prob, 2))

    return result
matchups = [
  ["Michigan", 1, "Lehigh", 16],
  ["Nebraska", 4, "Troy", 13],
  ["Houston", 2, "Akron", 15]
]
print(upset_probability(matchups))