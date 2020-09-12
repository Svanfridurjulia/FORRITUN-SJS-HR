number_to_multiply = int(input("Input number to multiply: ")) # Do not change this line
how_often = int(input("Input how often to multiply: ")) # Do not change this line

count = 0

for i in range(1,how_often+1):
    count = i * number_to_multiply
    print(count)

#1.Start with user input
#2.Create a counter
#3.Use a for loop to multiply every number from 1 to user input
#4.Multiply the numbers in the range with the user input. 
    #4a Use the counter 
#5.Print the counter