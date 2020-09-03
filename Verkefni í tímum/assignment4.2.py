highest = int(input("Input an int: "))
highest_1 = highest + 1
#bæti einum við svo að það prentist líka input talan

for i in range(1,highest_1):
    if i%3==0:
        print(i)
    else:
        continue
