def intersection(list_1, list_2):
    final_list = []
    for element in list_1:
        if element in list_2 and element not in final_list:
            final_list.append(element)
    return final_list







list_1 = input("Input a list of elements: ").split()
list_2 = input("input another list of elements: ").split()

final_list = intersection(list_1,list_2)
print(final_list)