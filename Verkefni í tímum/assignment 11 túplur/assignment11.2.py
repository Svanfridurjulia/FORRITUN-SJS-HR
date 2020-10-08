
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    a_list = [int(i) for i in a_list]
    return a_list
    

def even_sum(a_list):
    even_list = [int(i) for i in a_list if i%2 == 0]
    even_sum = sum(even_list)
    return even_sum


a_list = get_list()
print(even_sum(a_list))
