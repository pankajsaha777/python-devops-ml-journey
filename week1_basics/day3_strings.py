'''
✅ Main Script: day3_strings.py
Task:

Ask user to enter their full name.

Print:

Name in uppercase
Name in lowercase
Total number of characters (excluding spaces)
First and last character of the name
'''

name = input('Please enter your Full Name')

print(f'Your name in uppercase is {name.upper()}')
print(f'Your name in lowercase is {name.lower()}')
print(f'First character of your name is {name[0]}')
print(f'Last character of your name is {name[-1]}')
tot_char = len([char for char in name if not char.isspace()])
print(f'Total number of characters (excluding spaces) in your names are {tot_char}')