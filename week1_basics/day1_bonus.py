#Task Ask the user for name and age.
#Print a message showing their name and how old they will be in 10 years.

name = input('Please enter your name')
age = int(input('Please enter your age'))

future_age = age + 10

print(f'Hello {name}! You know you will be {future_age} years after 10 years')