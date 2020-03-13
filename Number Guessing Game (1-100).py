###Number Guessing Game

import random
rand_number= random.randint(0,100)
number_of_attempts=0

while True:

    guess=input('Please make a guess: ')
    if not guess:
        break
    try:
        y=int(guess)
    except ValueError:
        print('Your guess:', guess)
        print('Please enter a numeric input')
        continue

    if y < 0 or y > 100:
        print('Your guess:', y)
        print('Please make a guess between 0 and 100')
    elif y<rand_number:
        print('Your guess:', y)
        print('Larger')
        number_of_attempts+=1
    elif y>rand_number:
        print('Your guess:', y)
        print('Smaller')
        number_of_attempts += 1
    else:
        number_of_attempts += 1
        print('Your guess:', y)
        print('You correctly found the number in {} attempts'.format(number_of_attempts))
        break



