#!/usr/bin/pyhton3

def print_last_digit(number):
    last = number % 10 if number > 0 else number * (-1) % 10
    print('{}'.format(last), end='')
    return last
