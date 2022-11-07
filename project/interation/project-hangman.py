
# HangMan
word = 'serendipitous'

vowels = ['a','e','i','o','u']

#set current vowel count
vowel_count = 0

for character in word:
    if character in vowels:
        vowel_count += 1

print (f"Total vowel: {vowel_count}" )