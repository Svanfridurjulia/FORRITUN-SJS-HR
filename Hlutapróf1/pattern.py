max_int = int(input("Input max integer: "))

for i in range(1,max_int+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

#1.Start with user input
#2.Create a for loop with range from 1 to max_int +1, so that max_int is included in the range
#3.Create another for loop inside with range from 1 to i + 1, so that i is included in the range 
#4.Print j in the same line and create a new line after the inner for loop is finished