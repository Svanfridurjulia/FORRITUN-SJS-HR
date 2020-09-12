import math

start_int = int(input("Input starting integer: "))
count = start_int

while count >= 2:
    square_root = float(math.sqrt(count))
    count = square_root
    print(round(count,4))


#1.Start with user input and import math
#2. Create a counter that is equal to the user input
#3. Create a while loop > 2
#4. Calculate the square root, change to float to be able to round
#5. Change the value of the counter to the outcome of the square root calculations
#7. print the rounded the answer
