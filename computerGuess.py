import random, math

print(f'Lets play! take the range number that you want!')
x = int(input('Pick the lowest number that you want! '))
y = int(input('Pick the highest number that you want! '))

def computerGuess(x, y):
    low = x
    high = y
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L) or correct(C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay!, I guess your number, {guess}, correctly!')


computerGuess(x, y)


    