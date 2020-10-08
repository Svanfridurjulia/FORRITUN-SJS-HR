

def open_file(filename):
    opened_file = open(filename,"r")
    return opened_file

def make_list(opened_file):
    file_list = []
    for lines in opened_file:
        split_lines = lines.split()
        file_list.append(split_lines)
    return file_list


def count_words(file_list):
    word_count = 0
    punctuation_count = 0
    for lines in file_list:
        for element in lines:
            word_count += 1
            for chr in element:
                if chr == "," or chr == "." or chr == "!" or chr == "?":
                    punctuation_count += 1
    return word_count + punctuation_count



#main

filename = input("Enter filename: ")
try:
    opened_file = open_file(filename)
    file_list = make_list(opened_file)
    word_count = count_words(file_list)
    print(word_count)
except FileNotFoundError:
    print("File {} not found!".format(filename))

