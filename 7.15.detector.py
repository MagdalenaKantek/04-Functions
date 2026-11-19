def f(detector):
    people = 0
    max_people = 0

    for sign in detector:
        if sign == "+":
            people += 1
        elif sign == "-":
            people -= 1

        if people > max_people:
            max_people = people

    if max_people >= 3:
        return True
    else:
        return False

print(f("+-+++-+---"))
print(f("+-+-+-+-")) 
print(f("+-++-+--"))
print(f("+-++-++-+---")) 
