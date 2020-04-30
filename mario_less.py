#!/usr/bin/env python3
# pylint: disable = C0103
from sys import stdout
'''
This is my python implementation of the mario assignment from week 1.  This
environment I'm a bit more comfortable with.
'''
def main():
    '''
    This is where the short magic will be.  This will be much easier to implement
    in Python for me.
    '''
    x = 0
    while True:
        try:
            x = int(input('Requested height and width(1 - 8 only): '))
            if 0 < x < 9:
                break
            print('Number can only be between 1 and 8')
        except ValueError:
            print('Invalid input')

    for i in range(x):
        print((x - i - 1) * ' ', ('#' * (i + 1)))

if __name__ == "__main__":
    main()
