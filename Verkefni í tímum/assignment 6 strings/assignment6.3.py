a_str = input("Input a string: ")
lower_count = 0
upper_count = 0


for letter in a_str:
    if (letter.islower()):
        #Check if the letter is lower case
        lower_count = lower_count + 1
    elif (letter.isupper()):
        upper_count = upper_count + 1

print(lower_count, upper_count)

