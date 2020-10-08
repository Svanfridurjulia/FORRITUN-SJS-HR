def remove_whitespaces(opened_file):
    for line in opened_file:
        print(line.strip().replace(" ", ""), end = "")
    return True


file_name = input("Enter filename: ")

opened_file = open("data.txt", "r")
readfile = remove_whitespaces(opened_file)
print(readfile)

