'''
🔹 Optional Advanced Bonus: day3_advanced_bonus.py

Task:

Ask user for a string.

Print a frequency count of each character (ignore spaces).
'''

text = input('Enter a sentence').replace(' ','')
freq = {}

for char in text.lower():
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1

print('Frequency count of each character')
for char,count in freq.items():
    print(f'{char}:{count}')