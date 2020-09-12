num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int

while num_int >= 0:
    num_int = int(input("Input a number: "))  
    num_int1 = num_int
    if num_int1 > max_int:
        max_int = num_int
else:
    print("The maximum is", max_int)    # Do not change this line
