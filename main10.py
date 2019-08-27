#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') # prints 'Greetings!' Game begings
colors = ['red','orange','yellow','green','blue','violet','purple'] # gives you a selection of to choose possible answers (correct & incorrect)
play_again = ''
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'):   # begins the loop
    match_color = random.choice(colors) # picks a color for you
    count = 0
    color = ''
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()   # takes away case sensitivity
        count += 1  # adds 1 to how many times you've tried to get the right answer
        if (color == match_color):
            print('Correct!')   # prints 'Correct!'
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))  # tells you how many times you've tried so far
    print('\nYou guessed it in {0} tries!'.format(count))   # tells you how many times it took you to get the right answer
    if (count < best_count):   
        print('This was your best guess so far!')   # tells you that you made the new high score
        best_count = count
    play_again = input("\nWould you like to play again? ").lower().strip()  # asks if you would like to play again
print('Thanks for playing!') # prints 'Thanks for playing!' Game ends.