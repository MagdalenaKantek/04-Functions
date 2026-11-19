def f(expression):
    total = 0
    sign = 1

    for char in expression:
        if char == '-':
            sign = -1
        elif char == '+':
            sign = 1
        else:
            total += int(char) * sign

    return total

print(f("2+3"))  # returns 5
print(f("3+8+1"))  # returns 12
print(f("2+3-4+5-0"))  # returns 6