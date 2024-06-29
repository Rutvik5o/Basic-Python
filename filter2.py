marks=[54,33,67,37,73,3,63]


def failing(score):
    return score<60


result=filter(failing,marks)

print("Failing Scores",list(result))