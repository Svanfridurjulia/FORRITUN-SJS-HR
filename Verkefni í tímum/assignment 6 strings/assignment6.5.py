a_str = input("Input a string: ")

word_count = 1
letter_count = 0

for letter in a_str:
    if letter == ' ':
        word_count = word_count + 1
    elif letter.isalpha() or letter.isnumeric():
        letter_count = letter_count + 1

print("No. of letters: {}, no. of words: {}".format(letter_count,word_count))
