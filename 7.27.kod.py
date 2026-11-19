def f(product_code):
    total = 0

    for digit in product_code[:-1]:
        total += int(digit)

    control_digit = total % 7

    return control_digit == int(product_code[-1])


print(f("1082"))  # True
print(f("2035"))  # True
print(f("1114"))  # False
print(f("7071"))  # False