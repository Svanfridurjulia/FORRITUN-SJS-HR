def count_integers(integers,integer):
    count = 0
    for number in integers:
        if number == integer:
            count += 1
    return str(count)



integers = input("Input integers: ")
integer = input("Input a integer: ")
count = count_integers(integers,integer)
print("The integer {} appeared {} times".format(integer,count))