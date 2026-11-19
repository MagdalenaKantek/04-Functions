import months

month_number = int(input("Enter month number (1-12): "))
month_name = months.month(month_number)
print(f'The month corresponding to number {month_number} is {month_name}.')