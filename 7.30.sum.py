def sum_natural(n):

    if n == 1: #warunek zatrzymania rekurencji
        return 1  
    else:
        return n + sum_natural(n - 1) #dodajemy aktualną liczbę do sumy mniejszych liczb.


print(sum_natural(10))  # 55