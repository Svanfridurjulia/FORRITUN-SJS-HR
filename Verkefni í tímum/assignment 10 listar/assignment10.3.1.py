def add_word():
    word = ""
    while word != "x":
        word = input("Enter word to be added to list: ")
        if word != "x":
            first_list.append(word)

def word_list():
    for word in first_list:
        if len(word) > 1:
            if word[0] == word[-1]:
                second_list.append(word)

def print_second_list():
    for word in second_list:
        print(word)


first_list = []
second_list = []
add_word()
print(first_list)
word_list()
print_second_list()