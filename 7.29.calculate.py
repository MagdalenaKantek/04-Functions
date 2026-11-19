def factorial(n):
    # Warunek zatrzymania rekurencji
    if n == 0 or n == 1:   #silnia z 0 i silnia z 1 wynosi 1.
        return 1  

    # Wywołanie funkcji samej siebie
    if n > 1:
        return n * factorial(n - 1)  #wywołujemy tę samą funkcję ponownie, ale dla liczby mniejszej o 1


print(factorial(5))