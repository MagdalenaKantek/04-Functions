###
# Calculates the sum of the digits in a number
#
import math

def sum_digits(number):
    total = 0
    any_number = str(abs(number))
    for digit in any_number:
        total += int(digit)
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')