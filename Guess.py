import random


def computer_guess(x):
    low = 1
    high = x

    feedback = ''

    while feedback != 'c':
        guess1 = random.randint(low, high)

        feedback=input(f'Is {guess1} too high (h), or too low (l), or correct (c)')

        if feedback == 'h':
            high = guess1-1
        elif feedback == 'l':
            low = guess1+1

    print(f'Yay! The computer guessed your number, {guess1}, correctly!')


computer_guess(10)
    