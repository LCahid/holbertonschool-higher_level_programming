#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    d = {'+': add, '-': sub, '*': mul, '/': div}
    for op in d:
        print('{} {} {} = {}'.format(a, op, b, d[op](a, b)))
