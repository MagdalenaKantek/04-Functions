import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'2.54 cm is {converters.cm_to_inch(2.54)} inches')
print(f'2 feet and 3 inches is {converters.feet_inches_to_cm(2, 3)} cm')