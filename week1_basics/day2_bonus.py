'''
🎁 Bonus Script: day2_bonus.py

Task:

Ask user for a string.

Print:

The string in uppercase & lowercase.

Length of the string.

Whether the string is a number (digit check).

Reverse of the string.
'''


text = input('Enter a text or string')

print(f'Length of the string {text} is ',len(text))
if text.isdigit():
    print('The string that you entered is a digit')
else:
    print(f'The entered string {text} is not a digit')

print(f'reversed {text}: ',text[::-1])