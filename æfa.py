def open_file(filename):
    try:
        opened_file = open(filename,"r")
        return opened_file
    except FileNotFoundError:
        print("File {} not found".format(filename))
        main()


def make_lists(opened_file):
    parts_list = []
    for lines in opened_file:
        split_lines = lines.split()
        for elements in split_lines:
            parts_list.append(elements)
    print(parts_list)

filename = input("Enter filename for parts: ")
opened_file = open_file(filename)
make_lists(opened_file)






