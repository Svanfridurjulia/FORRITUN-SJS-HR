def list_to_int_tuple(a_list):
    number_list = []
    for number in a_list:
        try:
            number_int = int(number)
            number_list.append(number_int)
        except ValueError:
            continue
    return tuple(number_list)


a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_int_tuple(a_list)
print(a_tuple)