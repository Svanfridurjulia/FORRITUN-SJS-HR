name = input("Input a name: ")

last,first = name.split(", ")

first_initial = first[0]
first_initial = first_initial.capitalize()
#Get the first letter of the first name and capitalize

last_name = last.capitalize()

print("{}. {}".format(first_initial,last_name))

