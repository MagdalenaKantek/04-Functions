import number_range

number = int(input("Enter a number: "))
x = int(input("Enter the lower bound of the range: "))
y = int(input("Enter the upper bound of the range: "))  

result = number_range.is_in_range(number, x, y)
if result:
    print(f'The number {number} in the range <{x}, {y}>: yes.')
else:
    print(f'The number {number} in the range <{x}, {y}>: no.')