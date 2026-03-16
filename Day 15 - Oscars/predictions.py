def oscar_pool(predictions):
    
    actual = [
        "One Battle After Another",
        "Michael B. Jordan",
        "Jessie Buckley",
        "Paul Thomas Anderson"
    ]
    
    max_correct = -1
    winner = ""
    tie = False

    for friend in predictions:
        name = friend[0]
        correct = 0

        for i in range(4):
            if friend[i + 1] == actual[i]:
                correct += 1

        if correct > max_correct:
            max_correct = correct
            winner = name
            tie = False
        elif correct == max_correct:
            tie = True

    return "Tie" if tie else winner

predictions = [
  ["@sonny", "One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Ryan Cooger"],
  ["@brit896", "Marty Supreme", "Timothée Chalamet", "Jessie Buckley", "Josh Safdie"],
  ["@tylerwhit", "Sinners", "Michael B. Jordan", "Rose Byrne", "Paul Thomas Anderson"]
]
print(oscar_pool(predictions))