def make_grid(lines,length):
    for i in range(length):
        print()
        for i in range(lines):
            print("2",end=" ")

def print_lines(line_int,length)
    


lines = int(input("Input number of lines: "))
length = int(input("Input length of lines: "))
user_choice = input("Do you want to output a line (a) or output a column (b):")

if user_choice == 'a':
    lines_str = str(lines)
    line_int = int(input("Input a number in the range 1 <= x <= {}: ".format(lines_str)))
    print_lines(line_int,length)


make_grid(lines,length)