def my_strip(string,word):
    lower_case = string.lower()
    for words in lower_case:
        if word in lower_case:
            new_string = lower_case.replace(word,"")
    return new_string




string = input("Input a string: ")
word = input("Input a word to remove: ")
stripped_string = my_strip(string,word)
print(stripped_string)