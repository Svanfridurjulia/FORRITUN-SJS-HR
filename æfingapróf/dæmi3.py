def unique_list(set_list):
    unique_list = []
    for elements in set_list:
        if int(elements) not in unique_list:
            unique_list.append(int(elements))
    return unique_list


def sort_list(unique_list):
    return sorted(unique_list)

def intersection(list1,list2):
    intersection_list = []
    for elements in list1:
        if elements in list2:
            intersection_list.append(elements)
    return intersection_list

def union(list1,list2):
    union_list = list1
    for elements in list2:
        if elements not in union_list:
            union_list.append(elements)
    return sorted(union_list)


#Main

list_1 = input("Enter elements of a list separated by space: ").split()
list_2 = input("Enter elements of a list separated by space: ").split()

unique_list1 = unique_list(list_1)
sorted_list1 = sort_list(unique_list1)
print("Set 1:",sorted_list1)

unique_list2 = unique_list(list_2)
sorted_list2 = sort_list(unique_list2)
print("Set 2:",sorted_list2)

intersection_list = intersection(sorted_list1,sorted_list2)
print("Intersection:",intersection_list)

union_list = union(sorted_list1,sorted_list2)
print("Union:",union_list)