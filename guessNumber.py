import random
import math

print(f'Lets play! let me know the radius of the number!')
x = int(input('Pick the lowest number that you want! '))
y = int(input('Pick the highest number that you want! '))

def guess(x, y):
    random_number = random.randint(x, y)
    guess = 0

    while guess != random_number:
        guess = int(input(f"guess number between {x} and {y}: "))
        print(guess)
        if guess > random_number:
            print("Top high, guess again!")
        elif guess < random_number:
            print("Too low, guess again!")

    print(f"Yay, the correct the number is {random_number}")

guess(x, y)
