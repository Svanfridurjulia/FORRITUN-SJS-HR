def my_split(string, char):
    my_list = string.split(char)
    return my_list



string = input("Input a string: ")
char = input("Input a character to split at: ")
split_list = my_split(string,char)
print(split_list)