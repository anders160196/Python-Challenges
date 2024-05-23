import random #library

number = random.randrange(1, 10)
guess = int(input('Guess a number between 1 and 10: '))
attempts = 1


while guess != number:
    if number > guess:
        print('Bigger')
    if number < guess:
        print('Smaller')
    guess = int(input('New guess: '))
    attempts = attempts + 1

print('You won! Attempts:' +str(attempts))
