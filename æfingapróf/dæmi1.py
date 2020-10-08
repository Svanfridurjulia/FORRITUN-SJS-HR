def convert_to_float(string_list):
    float_list = []
    for element in string_list:
        float_list.append(float(element))
    return float_list


def remove_min(float_list):
    min1 = min(float_list)
    float_list.remove(min1)
    min2 = min(float_list)
    float_list.remove(min2)
    return float_list


def find_sum(final_list):
    final_sum = sum(final_list)
    return round(final_sum,1)





string_list = input("Enter scores separated by space: ").split()


if len(string_list) > 1:
    float_list = convert_to_float(string_list)
    final_list = remove_min(float_list)
    final_sum = find_sum(final_list)
    print("Sum of scores (two lowest removed):",final_sum)
else:
    print("At least two scores needed!")