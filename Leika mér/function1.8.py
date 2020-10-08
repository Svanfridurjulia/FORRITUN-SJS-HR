def open_file():
    name_list = []
    open_file = open("names.txt","r")
    for name in open_file:
        name_list.append(name)
    return name_list



def alphabetical_value(name_list):
    sum_alpha = 0
    for name in name_list:
        letter_sum = alpha_name(name)
        sum_alpha += letter_sum
    return sum_alpha

def alpha_name(name):
    letter_sum = 0
    for letter in name:
        if letter != "\n":
            letter_sum += ord(letter)
    return letter_sum



name_list = open_file()
sum_alpha = alphabetical_value(name_list)
print(sum_alpha)