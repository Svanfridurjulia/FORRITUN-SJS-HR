def make_list(string):
    new_list = list(string)
    return new_list

def sort_list(b_list):
    b_list.sort()
    return b_list

sentence = input("Input a sentence: ")

a_list = make_list(sentence)
print(a_list)
sorted_list = sort_list(a_list)
print(sorted_list)