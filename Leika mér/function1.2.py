def sum(integer_list):
    sums = 0
    for number in integer_list:
        sums += int(number)
    return sums

def find_mean(sums,integer_list):
    length = len(integer_list)
    mean = sums/length
    return mean





#main

integer_list = input("Enter numbers:").split()
sums = sum(integer_list)
print("Sum:",sums)
mean = find_mean(sums,integer_list)
print("Mean:",mean)
