
def process_all_files(filename_list):
    """Function that calls another function to open the file/s"""
    for filename in filename_list:
        open_files(filename)

def open_files(filename):
    """Function that returns the open file or returns error message if the file is not found."""
    try:
        opened_file = list(open(filename, "r"))
        call_functions(opened_file,filename)
    except FileNotFoundError:
        print("\nFile {} not found".format(filename))

def call_functions(opened_files,filename):
    """Function that calls other functions and returns nothing"""
    number_list = remove_str(opened_files)
    if number_list == None:
        number_list = []
    processed_list = process_list(number_list)
    print_sequence(processed_list,filename)
    find_print_cumulative_sum(processed_list)
    sort_print_sequence(processed_list)
    number_count = count_numbers(processed_list)
    median = find_median(processed_list,number_count)
    print_median(median)


def remove_str(opened_file):
    """Function that removes words and letters from list and returns the new list"""
    number_list = opened_file
    count = len(number_list)
    for number in range(count):
        number += 1
        for element in opened_file:
            if element >= 'a':
                number_list.remove(element)
    return number_list

def process_list(opened_file):
    """Function that changes the number in the list to float and returns the new list"""
    number_string = ""
    try:
        for elements in opened_file:
            float_element = float(elements)
            number_string += str(float_element) + " "
    except ValueError:
        pass
    return number_string.split()
        

def print_sequence(number_list,filename):
    """Function that prints the sequence and returns nothing"""
    print("\nFile {}".format(filename))
    print("\tSequence:")      
    string = " "
    number_string = string.join(number_list)
    print("\t\t{}".format(number_string),end=" ")


def find_print_cumulative_sum(number_list):
    """Function that finds and prints the rounded cumulative sum and returns nothing"""
    print("\n\tCumulative sum:")
    sum_count = 0
    print("\t\t",end="")
    for element in number_list:
        sum_count += float(element)
        rounded_result = round(sum_count,4)
        print(rounded_result,end=" ")
    print()

def sort_print_sequence(number_list):
    """Function that sorts and prints the sequence and returns nothing"""
    print("\tSorted sequence:")
    string = " "
    number_list.sort(key=float)
    sorted_string = string.join(number_list)
    print("\t\t{}".format(sorted_string),end=" ")

def count_numbers(number_list):
    """Function that finds and returns the number of elements in the list"""
    count = len(number_list)
    return count

def find_median(number_list,number_count):
    """Function that calculates and rounds the median and returns it"""
    if number_count > 0:
        if number_count % 2 == 0:
            middle_number1 = number_list[number_count//2]
            middle_number2 = number_list[number_count//2 - 1]
            median = (float(middle_number1)+float(middle_number2))/2
        else:
            median = float(number_list[number_count//2])
        rounded_median = round(median,4)
    else:
        rounded_median = 0
    return rounded_median  

def print_median(median):
    """Function that prints the median and returns nothing"""
    print("\n\tMedian:")
    if median > 0:
        print("\t\t{}".format(median))  
    else:
        print("")




filename_list = input("Enter filenames: ").split()
process_all_files(filename_list)
    

