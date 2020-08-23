"""Matching brackets
Write a simple brackets checker that, given a string,
returns 'OK' if all the brackets are used correctly, and 'ERROR' otherwise.
"""
from collections import deque

my_stack_open = deque()
my_stack_close = deque()

line = input()

for i in line:
    if i == '(':
        my_stack_open.append(i)
    elif i == ')':
        my_stack_close.append(i)

    if len(my_stack_close) > len(my_stack_open):
        print('ERROR')
        break

if len(my_stack_open) == len(my_stack_close):
    print('OK')
elif len(my_stack_open) > len(my_stack_close):
    print('ERROR')
