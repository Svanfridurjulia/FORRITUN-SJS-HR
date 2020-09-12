my_int = int(input('Give me an int >= 0: '))

bin_str = ''
number = my_int

if my_int == 0:
    bin_str = '0'

while number > 0:
    if number % 2 == 0:
        bin_str = bin_str + '0'
        number = number//2
    else:
        bin_str = bin_str + '1'
        number = number//2


bin_str = bin_str[::-1]
#To reverse the string

print("The binary of {} is {}".format(my_int,bin_str))

