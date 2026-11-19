def f(dice):
    previous = dice[0]
    current_count = 1
    max_count = 1
    result = previous

    for roll in dice[1:]:
        if roll == previous:
            current_count += 1
        else:
            current_count = 1
            previous = roll

        if current_count > max_count:
            max_count = current_count
            result = previous

    return result


print(f("5233165554211"))  # 5
print(f("2133"))           # 3