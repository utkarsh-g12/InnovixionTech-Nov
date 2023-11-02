# Import "Random" library for generating a random number
import random

# using "randint" function for generating a random number between a range
generated_number = random.randint(1, 100)

'''using "For" Loop for fixing the number of attempts 
In this game by default number of attempts are 3'''

left_chances = 3

while left_chances > 0:
    left_chances -= 1
    guess_number = int(input("Enter a number "))
    if guess_number < generated_number:
        print("You guessed wrong!! Try Harder")
        print("Hint : choose a large number", end="\n")
        print(left_chances, " more chances left", end="\n")
    elif guess_number > generated_number:
        print("Number guess is wrong!! Try Harder")
        print("Hint : choose a small number", end="\n")
        print(left_chances, " more chances left", end="\n")
    else:
        print("Number guessed right")
        break
    if left_chances == 0:
        print("You Lost the Game")
        print("Game is Over")
