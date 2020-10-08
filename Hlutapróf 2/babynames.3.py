def open_file(filename):
    '''A function which tries to open the file and return it if the file is found. Otherwise it prints out error message'''
    try:
        opened_file = open(filename,"r")
        return opened_file
    except FileNotFoundError:
        print("File {} not found".format(filename))

    

def make_list(opened_file):
    '''A function which takes the opened file and makes lists within a list and returns that list'''
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

def first_five_list(final_list):
    '''A function which creates a list of the first five girl names and onether list of the first five boy names and returns both lists'''
    girl_list=[]
    boy_list = []
    for lines in final_list:
        if len(girl_list) < 5:
            girl_list.append(lines[-2:])
        if len(boy_list) < 5:
            boy_list.append(lines[1:3])
    return girl_list, boy_list

def list_frequencies(final_list):
    '''A function that makes two seperate lists, one with all the girl frequencies and the other with all the boy frequencies, and returns them'''
    b_list_frequencies = []
    g_list_frequencies = []
    #b stands for boys and g for girls
    for lines in final_list:
        b_list_frequencies.append(lines[2])
        g_list_frequencies.append(lines[4])
    return b_list_frequencies, g_list_frequencies

def call_functions(opened_file):
    '''A function which calls other functions and returns nothing'''
    baby_list= make_list(opened_file)
    final_list = convert_to_int(baby_list)
    print_list = first_two(final_list)
    girl_list, boy_list = first_five_list(final_list)
    b_list_frequencies, g_list_frequencies = list_frequencies(final_list)
    frequency_boys, frequency_girls = find_frequency(b_list_frequencies,g_list_frequencies)
    print_func(print_list,boy_list,girl_list,frequency_boys,frequency_girls)

def find_frequency(boy_list,girl_list):
    '''A function which finds the total frequency of all boy names and then of all the girl names and returns them '''
    boy_frequency = sum(boy_list)
    girl_frequency = sum(girl_list)
    return boy_frequency, girl_frequency


def print_func(list1,list2,list3,frequency_boys,frequency_girls):
    '''A Function which prints the output and returns nothing'''
    print(list1)
    print(list2)
    print(list3)
    print("Total frequency of boy names:",frequency_boys)
    print("Total frequency of girl names:",frequency_girls)



#Main

filename = input("Enter file name: ")
opened_file = open_file(filename)
if opened_file != None:
    call_functions(opened_file)
    