def my_range(start,end, inc = "1"):   
    number = start
    range_list = []
    range_list.append(start)
    while number < (end):
        number += int(inc)
        if number < end:
            range_list.append(number)
    return range_list


start = int(input("Enter a start number: "))
end = int(input("Enter a end number: "))
inc = int(input("Enter iteration: "))

range_list = my_range(start,end,inc)
print(range_list)
