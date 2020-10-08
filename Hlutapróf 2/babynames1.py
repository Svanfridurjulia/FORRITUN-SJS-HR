def open_file(filename):
    '''A function which tries to open the file and return it if the file is found. Otherwise it prints out error message'''
    try:
        opened_file = open(filename,"r")
        return opened_file
    except FileNotFoundError:
        print("File {} not found".format(filename))
    

def make_list(opened_file):
    '''A function which takes the opened file and makes lists within a list of every line and returns that list'''
    baby_list = []
    for lines in opened_file:
        line_list = lines.split("\t")
        baby_list.append(line_list)
    return baby_list
            

def convert_to_int(baby_list):
    '''A function which converts the numbers to int and returns a list of lists containing both strings and ints'''
    final_list = []
    for lists in baby_list:
        list1 = []
        for elements in lists:
            try:
                list1.append(int(elements))
            except ValueError:
                list1.append(elements)
        final_list.append(list1)
    return final_list

def first_two(final_list):
    '''A function which creates a list with only the first two elements in final_list and returns it'''
    print_list = []
    for lists in final_list:
        if len(print_list) < 2:
            print_list.append(lists)
    return print_list


def call_functions(opened_file):
    '''A function which calls other functions and returns nothing'''
    baby_list = make_list(opened_file)
    final_list = convert_to_int(baby_list)
    print_list = first_two(final_list)
    print_func(print_list)

def print_func(list1):
    '''A Function which prints the output and returns nothing'''
    print(list1)

#Main

filename = input("Enter file name: ")
opened_file = open_file(filename)
if opened_file != None:
    call_functions(opened_file)

