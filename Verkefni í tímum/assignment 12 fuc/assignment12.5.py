def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
        

def proccess_input(integers):
    error = False
    try:
        int_list = []
        number = ""
        for ints in integers:
            if ints == ",":
                int_list.append(int(number))
                number = ""
            else:
                number += ints
                if int(ints) < 0:
                    error = True
                    break
        int_list.append(int(number))
    except ValueError:
        print("Incorrect input!")
        exit()
    if error == True:
        print("Incorrect input!")
        exit()
    else:
        return int_list


def print_list(int_list):
   print("Input list:",int_list)

def sort_list(int_list):
    print("Sorted list:",sorted(int_list))

def print_prime(int_list):
    prime_list = []
    for n in int_list:
        false_true = is_prime(n)
        if false_true == True:
            if not n in prime_list:
                prime_list.append(n)
    print("Prime list:",sorted(prime_list))    

def find_min(int_list):
    min_val = min(int_list)
    return str(min_val)

def find_max(int_list):
    max_val = max(int_list)
    return str(max_val)

def find_average(int_list):
    length = len(int_list)
    average = (sum(int_list))/length
    rounded_average = '{:.2f}'.format(round(average,2))
    return rounded_average


# The main program starts here

integers = input("Enter integers separated with commas: ")

int_list = proccess_input(integers)
print_list(int_list)
sort_list(int_list)
print_prime(int_list)
min_val = find_min(int_list)
max_val = find_max(int_list)
average = find_average(int_list)
print("Min: {}, Max: {}, Average: {}".format(min_val,max_val,average))
