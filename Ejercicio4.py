import re 
from operator import itemgetter
from decimal import Decimal, ROUND_HALF_UP
def do_math(string):
    numbers = string.split()
    num_dict ={}
    for number in numbers:
        letter = re.search("[a-zA-Z]",number).group()
        num_dict[number] = letter

    num_dict = sorted(num_dict.items(), key=itemgetter(1))
    result = None
    for num in num_dict:
        if result == None:
            result = Decimal(num[0])
        else:
            result = result * Decimal(num[0])
    return result.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    

 