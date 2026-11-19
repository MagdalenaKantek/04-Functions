import letters

text = "You never get a second chance to make a first impression"
letter = 'e'

letter_count = letters.count_letters(text, letter)

print(f'The letter "{letter}" appears {letter_count} times in the text: "{text}"')