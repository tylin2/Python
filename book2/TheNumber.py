# This is a guess the number game.

import random

print('I am thinking of a number between 1 and 20.')
ans = random.randint(1,20)
gu = '-1'
count = 0;
while ans != int(gu):
    print('Take a guess.')
    gu = input()
    if int(gu) < ans :
        print('Your guess is too low.')
        count = count + 1
    elif int(gu) > ans :
        print('Your guess is too high.')
        count = count + 1
    else:
        print('Good job! you guessed my number in ' + str(count) + ' guesses!')


'''
# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
'''
