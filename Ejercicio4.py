import re 
from operator import itemgetter
from decimal import Decimal, ROUND_HALF_UP
def do_math(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b