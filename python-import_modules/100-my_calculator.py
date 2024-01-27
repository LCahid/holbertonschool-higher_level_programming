#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argc = len(argv) - 1
    if argc != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    d = {'+': add, '-': sub, '*': mul, '/': div}
    try:
        print('{} {} {} = {}'.format(a, op, b, d[op](a, b)))
        exit(0)
    except KeyError:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
