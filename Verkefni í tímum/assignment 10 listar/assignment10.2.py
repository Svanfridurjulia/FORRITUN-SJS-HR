import string

def unique():
    for chr in sentence:
        if chr.isalpha():
            first_letters.append(chr)
        
    for char in first_letters:    
        if not (char in unique_letters):
            unique_letters.append(char)

sentence = input("Input a sentence: ")


unique_letters = []
first_letters = []
unique()
print("Unique letters:", unique_letters)
