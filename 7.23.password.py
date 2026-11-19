def f(password):
    if len(password) < 6:
        return False

    for letter in password:
        if password.count(letter) > 1:
            return False

    return True

print(f("ax15")) 
print(f("book123")) 
print(f("A2water3")) 
print(f("qwerty")) 
print(f("")) 
