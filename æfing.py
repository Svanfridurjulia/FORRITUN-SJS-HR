
def find_and_replace(string,find_string,replace_string):
    if find_string in string:
        final_string = string.replace(find_string,replace_string)
        return final_string
    else:
        print("Invalid input!")


def remove(string,remove_string):
    if remove_string in string:
        final2_string = string.replace(remove_string,"")
        return final2_string
    else:
        print("Invalid input!")




first_string = input("Please enter a string: ")
print("""\t1. Find and replace
\t2. Find and remove
\t3. Remove unnecessary spaces
\t4. Encode
\t5. Decode
\tQ. Quit""")
option = input("Enter one of the following: ")

if option == "1":
    find_string = input("Please enter substring to find: ")
    replace_string = input("Please enter substring to replace with: ")
    final1_string = find_and_replace(first_string,find_string,replace_string)
    print(final1_string)
elif option == "2":
    remove_string = input("Please enter substring to remove: ")
    final2_string = remove(first_string,remove_string)
    print(final2_string)