import string


def open_file(filename):
    opened_file = open(filename, "r")
    return opened_file

def process_file(opened_file):
    word_list = []
    for line in opened_file:
        line = line.strip().split()
        for word in line:
            word = word.strip(string.punctuation)
            word_list.append(word)
    return word_list


def unique_list(word_list):
    data = []
    for word in word_list:
       if data.count(word) < 1:
            data.append(word)
    return data

def sort_list(unique):
    print(sorted(unique))






filename = input("Enter filename: ")
opened_file = open_file(filename)
word_list = process_file(opened_file)
unique = unique_list(word_list)
sort_list(unique)