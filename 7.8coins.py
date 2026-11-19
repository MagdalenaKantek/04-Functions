def min_coins(amount_to_pay):
    coins = 0

    while amount_to_pay >= 5:
        amount_to_pay -= 5
        coins += 1

    while amount_to_pay >= 2:
        amount_to_pay -= 2
        coins += 1

    while amount_to_pay >= 1:
        amount_to_pay -= 1
        coins += 1

    return coins

amount = int(input("Enter amount to pay: "))

result = min_coins(amount)

print(f'Minimum number of coins: {result}')