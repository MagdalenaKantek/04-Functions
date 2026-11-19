def f(x, y):
    total = 0

    for number in range(x, y + 1):
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total += number

    return total

print(f(1,20))  # returns 24
print(f(10,30))  # returns 48