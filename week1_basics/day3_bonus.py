'''
🎁 Bonus Script: day3_bonus.py

Task:

Ask user for a sentence.

Print:

Number of words
Number of vowels
Reverse of the sentence
'''

sentence = input('Enter a sentence')

words_count = len(sentence.split())
'''
Basic method for counting vowels
vowels = 0
for vow in sentence.lower():
    if vow in 'aeiou':
       vowels+=1
'''
# Pyhon 1 liner for counting vowels in sentence using list comprehension and generator
vowels = sum([1 for vow in sentence.lower() if vow in 'aeiou'])
print(f'Number of words is {words_count}')
print(f'number of vowels is {vowels}')
print(f'Sentence in reverse is {sentence[::-1]}')