def open_file(filename):
    try:
        opened_file = open(filename,"r")
        return opened_file
    except FileNotFoundError:
        print("File {} not found".format(filename))
        main()


def make_list(opened_file):
    part_list = []
    for lines in opened_file:
        split_lines = lines.split()
        for elements in split_lines:
            part_list.append(elements)
    return part_list

def split_list(part_list):
    length = len(part_list)
    middle = length/2
    name_list = []
    weight_list = []
    for elements in part_list:
        if len(name_list) < middle:
            name_list.append(elements)
        else:
            weight_list.append(float(elements))
    return name_list, weight_list

def list_of_tuple(list1,list2):
    tuple_list = []
    for num in range(len(list1)):
        element_list = []
        element_list.append(list1[num])
        element_list.append(list2[num])
        tuple_list.append(tuple(element_list))
    return tuple_list





def call_functions_parts(filename):
    opened_file = open_file(filename)
    parts_list = make_list(opened_file)
    name_list, weight_list = split_list(parts_list)
    tuple_list = list_of_tuple(name_list, weight_list)
    printing(tuple_list)

def call_functions_grades(filename):
    opened_file = open_file(filename)
    grades_list = make_list(opened_file)
    print(grades_list)

def printing(tuple_list):
    print(tuple_list)








#Main
def main():
    filename_parts = input("Enter filename for parts: ")
    call_functions_parts(filename_parts)
    filename_grades = input("Enter filename for grades: ")
    call_functions_grades(filename_grades)

main()