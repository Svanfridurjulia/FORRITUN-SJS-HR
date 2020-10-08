def convert_int(elements):
    int_list = []
    new_elements = elements.replace(",","")
    for number in new_elements:
        try:
            int_list.append(int(number))
        except ValueError:
            print("Error: enter only integers.")
            exit()
    return int_list


def count_consecutive(int_list):
    consecutive_check = int(input("Consecutive check: "))
    counter = 0
    for elements in int_list:
        if elements == consecutive_check:
            counter += 1
    return counter

def false_true(counter):
    if counter >= 2:
        print(True)
    else:
        print(False)




elements = input("Enter elements of list separated by commas: ")
int_list = convert_int(elements)
counter = count_consecutive(int_list)
false_true(counter)


