def remove_evens(a_list):
    for number in a_list:
        for number in a_list:
            if number%2 == 0:
                a_list.remove(number)



def remove_evens2(b_list):
    b_list = [i for i in b_list if i%2 != 0]
    return b_list


a_list = [1,2,2,3,4,5]
print(a_list)
remove_evens(a_list)
print(a_list)
    
b_list = [1,2,3,4,4,5,6,7,8,9,10]
c_list = remove_evens2(b_list)
print(b_list)
print(c_list)