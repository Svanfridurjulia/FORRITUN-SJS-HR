
def add_word(string):
    new_string = list(string)
    new_list = new_string.append(new_string)
    return new_list

def words(word):
    if word[0] == word[-1]:
        return word


def print_words(string):
    for word in string:
        print(word)

word = input("Enter a word to be added to the list: ")
string_list = " "

while word != 'x':
    first_list = add_word(word)
    if len(word) > 1:
        second_list = words(word)
        string_list += second_list


    word = input("Enter a word to be added to the list: ")


print(first_list)
print_words(string_list)