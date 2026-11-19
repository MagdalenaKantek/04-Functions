def f(text):
    result = ''

    for char in text:
        if result != '':
            result += '-'
        result += char

    return result

print(f("Univesity"))  # returns "U-n-i-v-e-r-s-i-t-y"
print(f("UE"))  # returns "U-E"
print(f("x"))  # returns "x"
print(f(""))  # returns ""