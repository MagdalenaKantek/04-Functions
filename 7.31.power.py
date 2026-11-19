def power(x, n):  #Przykład: power(5, 3) oznacza (5**3)
    if n == 0:
        return 1 
    else:
        return x * power(x, n - 1)  #mnożymy x przez wynik kolejnego wywołania funkcji, w którym wykładnik jest mniejszy o 1


print(power(5, 3))  # 125