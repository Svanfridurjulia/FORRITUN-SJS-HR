
#1.Start
#2.user inputs an integer
#3.use max_int as a counter for num_int
#4.use while loop to keep the program running until a negative integer is entered
#5.use num_int1 to compare the user input inside the while loop with the user input outside the while loop
#6.rewrite max_int as the max integer
#7.print the max_int


num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int

while num_int >= 0:
    num_int = int(input("Input a number: "))  
    num_int1 = num_int
    if num_int1 > max_int:
        max_int = num_int
else:
    print("The maximum is", max_int)    # Do not change this line

