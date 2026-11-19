def f(number1,number2,operator):
       if operator =="+":
          result = number1 + number2
       elif operator =="%":
          result = number1 % number2
       elif operator =="**":
          result = number1 ** number2
       elif operator =="*":
          result = number1 * number2
       elif operator == "-":
          result = number1 - number2
       else:
          print('Invalid operator')
    
       return result

print(f(2,3, "+"))  # returns 5
print(f(2,3, "%"))  # returns 2
print(f(2,3, "**"))  # returns 8
print(f(2,3, "*"))  # returns 6
print(f(2,3, "-"))  # returns -1