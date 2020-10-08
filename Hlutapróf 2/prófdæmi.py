def sum_number(n):
    '''A function which finds the sum of 1..n and returns it'''
    sum_of_range = 0
    for num in range (1,n+1):
        sum_of_range += num
    return sum_of_range
    

def product(n):
    '''A function which finds the product of 1..n and returns it'''
    multi = 1
    for num in range(1,n+1):
        multi = multi * num
    return multi

def print_choices():
    '''A function which prints the choices and gets the choice from the user and returns it''' 
    print("""1: Compute the sum of 1..n
2: Compute the product of 1..n
9: Quit""")
    choice = input("Choice: ")
    return choice

def choice_1(int_list):
    '''A function for the choice 1 which calls the sum function and prints out the sum, returns nothing'''
    sum_of_numbers = sum_number(int_list)
    print("The result is:",sum_of_numbers)

def choice_2(int_list):
    '''A function for the choice 2 which calls the product function and prints out the product, returns nothing'''
    product_of_numbers = product(int_list)
    print("The result is:",product_of_numbers)


def choices(choice, n):
    '''A function which calls other functions depending on what the user choice is and returns nothing'''
    if choice == "1":
        choice_1(n)
    elif choice == "2":
        choice_2(n)
    


#Main
choice = print_choices()
while choice != "9":
    if choice == "1" or choice == "2":
        try:
            n = int(input("Enter value for n: "))
            choices(choice, n)
        except ValueError:
            pass
    choice = print_choices()
        
