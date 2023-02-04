# This code runs a program that wants you to guess the number between 1 - 10. The max points you will have is 100 if you find the number in your first guess. 
# And you input the number of life points you want to have. For example, If you input 5 then each guess will cost you 20 points. Good luck :d

import random

def guess_the_number():

    number = random.randint(1, 10)
    life_points = int(input("How many life point you want to have?"))
    life = life_points
    counter = 0

    while life > 0:
        life -= 1
        counter += 1
        guess = int(input("Input your guess"))
        if (number == guess):
            print(f" Nice! You've found the number in your {counter}th time. Total points: {100 - (100/life_points) * (counter-1)}")
            break
        elif number > guess:
            print("Higher")
        else:
            print("Lower")

        if life == 0:
            print(f"You don't have any life points. The number was {number}")

guess_the_number()
