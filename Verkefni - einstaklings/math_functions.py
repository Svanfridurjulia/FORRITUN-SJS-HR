#Write three differenct functions, one for each choice
    #sum_natural
    #sum_fibonacci
    #approximate_euler
#Create a input string
#Use a while loop to keep the program running until the user inputs 'X'
#Use if and elif statements to call the functions and print out correct output

options = print("""Please choose one of the options below:
a. Display the sum of the first N natural numbers. 
b. Display the sum of the first N Fibonacci numbers. 
c. Display the approximate value of e using N terms.
x. Exit from the program.""")

user_choice = input("Enter option: ")


while user_choice != 'x':

    def sum_natural(n_str):
        '''Calculates the natural sum of n_str and returns the sum'''
        if n_str >= 'a':
            #if the user input is something else than numbers the function returns none
            return None
        n_int = int(n_str)
        if n_int >= 2:
            natural_sum = int((n_int*(n_int+1))/2)
                        #making sure that it is not a float
            return natural_sum
    
    def sum_fibonacci(n_str):
        '''Calculates the sum of the first n_str numbers in a fibonacci sequence and returns the sum'''
        if n_str >= 'a':
            return None
        n_int = int(n_str)
        num1 = 0
        num2 = 1
        fibonacci_sum = 1
        if n_int >= 2:
            for num3 in range(n_int-2):
                num3 = num1 + num2
                num1 = num2
                num2 = num3
                fibonacci_sum +=num3
                #the sum of the sequence
            return fibonacci_sum
    
    def approximate_euler(n_str):
        '''Calculates the Euler number of the first n_str numbers and returns the result rounded to 5 decimal digits'''
        if n_str >= 'a':
            return None
        euler = 1
        number2 = 1
        n_int = int(n_str)
        if n_int >= 2:
            for number in range(1,n_int):
                number3 = number * number2
                euler += 1/(number3)
                number2 = number3
                #number2 is now the value of the numbers that have been multiplied together and then gets multiplied by number
            round_euler = round(euler,5)
            return round_euler


    if user_choice == 'a':
        input_n = input("Enter N: ")
        sum_return = sum_natural(input_n)
        #Calling the function
        if sum_return != None:
            print("Natural number sum:", sum_return)
        else:
            print("Error: {} was not a valid number.".format(input_n))
    elif user_choice == 'b':
        input_n = input("Enter N: ")
        fibonacci_return = sum_fibonacci(input_n)
        #Calling the function
        if fibonacci_return != None:
            print("Fibonacci sum:", fibonacci_return)
        else:
            print("Error: {} was not a valid number.".format(input_n))
    elif user_choice == 'c':
        input_n = input("Enter N: ")
        euler_return = approximate_euler(input_n)
        #Calling the function
        if euler_return != None:
            print("Euler approximation:", euler_return)
        else:
             print("Error: {} was not a valid number.".format(input_n))
    else:
        print("Unrecognized option {}".format(user_choice))
        print("""Please choose one of the options below:
a. Display the sum of the first N natural numbers. 
b. Display the sum of the first N Fibonacci numbers. 
c. Display the approximate value of e using N terms.
x. Exit from the program.""")
    
    user_choice = input("Enter option: ")






            








