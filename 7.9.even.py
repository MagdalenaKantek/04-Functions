def f(number, even):
    total = 0

    for digit in str(abs(number)):
        if even == True and int(digit) % 2 == 0:
            total += int(digit)
        elif even == False and int(digit) % 2 != 0:
            total += int(digit)

    return total

print(f(3124, True))
print(f(3124, False))
print(f(20576, False))
print(f(20576, True))