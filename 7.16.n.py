def f(n):
    previous = 0
    current = 1
    
    if n == 1:
        return 0 
    
    for i in range (n - 2):
        result = current + previous
        previous = current
        current = result
    return current

print(f(1))  # 0
print(f(5))  # 3
print(f(9))  # 21