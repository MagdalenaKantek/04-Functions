import binary

binary_number = input("Enter a binary number: ")
if binary.is_binary(binary_number):
    print(f'The number {binary_number} is a binary number: True.')
else:
    print(f'The number {binary_number} is a binary number: False.')
