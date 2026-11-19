def f(n):
    count = 0
    number = 2

    while count < n:
        is_prime = True

        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            count += 1
            if count == n:
                return number

        number += 1

print(f(1))  # 2
print(f(5))  # 11