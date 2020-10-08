choice = input("Input f|a|b (fibonacci, abundant or both): ")
number_1 = 0
number_2 = 1

if choice == 'f' or choice == 'b':
    sequence_length = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence: ")
    print("-------------------")
    print(number_1)
    #To get the first 0 in the sequence
    print(number_2)
    #To get the first 1 in the sequence
    for i in range(sequence_length-2):
        sum = number_1 + number_2
        number_1 = number_2
        #makes the sequence carry on
        number_2 = sum
        print(sum)
    


if choice == 'a' or choice == 'b':
    max_number = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")
    for number in range(1,max_number+1):
        total = 0
        #counter
        for num in range(1,number):
            #finds the divisors for each number
            if number%num == 0:
                total += num
        if total > number:
            print(number)
