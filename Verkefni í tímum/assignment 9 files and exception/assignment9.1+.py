def open_file_a(filename):
    file_a = open(filename,"r")
    return file_a

def open_file_b(filename):
    file_b = open(filename,"r")
    return file_b


def print_lines(file1,file2):
    line1 = ""
    for chr in file1:
        line1 += chr
        if chr == ("\n"):
            print(line1)
            line2 = ""
            for chr in file2:
                line2 += chr
                if chr == ("\n"):
                    print(line2)
                    line1 = ""
                    line2 = ""
                    break



file_name_a = input("First file: ")
file_name_b = input("Second file: ")

file_a = open_file_a(file_name_a)
file_b = open_file_b(file_name_b)