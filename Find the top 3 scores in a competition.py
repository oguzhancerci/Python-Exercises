# This code returns the first, second and third highest scores in a competition where the number of competitors are determined by inputs.
# Each of their score determined randomly.

import random

def contest():
    num_contender = int(input("How many contenders are there? "))
    scores = set()

    print("Contender's Scores: ")
    for i in range(num_contender):
        while len(scores) < i + 1:
            score = random.randint(1, 100)
            scores.add(score)
        print(score)
    scores = list(scores)
    scores.sort(reverse=True)
    if len(scores) < 2:
        print("Number of contenders can not be lower than 2")
    else:
        print("###############")
        print("First contender's score is: " + str(scores[0]))

        print("Second contender's score is: " + str(scores[1]))

        print("Third contender's score is: " + str(scores[2]))


contest()
