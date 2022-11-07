# While Loop
# unlike a For loop, needs the loop variable to be created and initialized beforehand


# while loop = the length of the sequnce determins the numbers of repetitions
vowels = ['a','e','i','o','u']

vowels_length = len(vowels)
print(vowels_length)

i = 0


while i < vowels_length:
    print(vowels[i])
    i += 1