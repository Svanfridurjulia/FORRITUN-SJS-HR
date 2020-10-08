def get_scores():
    list_scores = input("Enter scores separated by space: ").split()
    length = len(list_scores)
    if length > 1:
        return list_scores
    else:
        print("At least two scores needed!")


def convert_to_float(list_scores):
    float_list = []
    for number in list_scores:
        float_number = float(number)
        float_list.append(float_number)
    return float_list

def remove_two_min(float_list):
    min_number1 = min(float_list)
    float_list.remove(min_number1)
    min_number2 = min(float_list)
    float_list.remove(min_number2)
    return float_list
        

def print_sum(final_list):
    final_sum = sum(final_list)
    print("Sum of scores (two lowest removed):",final_sum)
    


list_scores = get_scores()
float_list = convert_to_float(list_scores)
final_list = remove_two_min(float_list)
print_sum(final_list)