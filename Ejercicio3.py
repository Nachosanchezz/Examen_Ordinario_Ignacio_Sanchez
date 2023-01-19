numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def numbers_of_letters(n):

    name = ''.join(numbers[i] for i in map(int, str(n)))
    return (name) + (numbers_of_letters(len(name)) if len(name) > 1 else '')
    






