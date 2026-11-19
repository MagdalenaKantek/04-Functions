def f(number):
    number_str = str(abs(number))
    total = 0

    for digit in number_str:
        if number_str.count(digit) > 1:
            total += int(digit)

    return total


print(f(1027))       # 0
print(f(230335))     # 9
print(f(513553007))  # 21