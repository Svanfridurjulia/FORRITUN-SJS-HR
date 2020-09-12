length = int(input("Input the length of series: "))
the_sum = 0
count = 2
addition = 6
for i in range(length):
    the_sum += count
    if count > 0:
        print(count)
        count = count - addition
        addition += 4
    elif count < 0:
        print(count)
        count = count + addition
        addition += 4
        
    
print("Sum:",the_sum)






