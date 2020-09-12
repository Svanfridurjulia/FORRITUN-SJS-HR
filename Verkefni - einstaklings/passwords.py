Min_chr = 6
Max_chr = 20
#Constants

password_str = input("Enter a new password: ")

password_counter = 0
valid_counter = 0
invalid_counter = 0


while password_str != 'q':
    upper_counter = 0
    lower_counter = 0
    digit_counter = 0
    password_length = 0
    for letter in password_str:
        if letter.islower():
            lower_counter = lower_counter + 1
        if letter.isupper():
            upper_counter = upper_counter + 1
        if letter.isdigit():  
            digit_counter = digit_counter +1 
        #Count how many lowercase and uppercase letters and how many digits in string
        password_length = len(password_str)
    if Min_chr <= password_length <= Max_chr:
        if lower_counter < 1:
            print("At least one lower case letter needed")
        if upper_counter < 1:
            print("At least one upper case letter needed")
        if digit_counter < 1:
            print("At least one number needed")
        if lower_counter < 1 or upper_counter < 1 or digit_counter < 1:
            invalid_counter = invalid_counter + 1
            
        if  digit_counter >= 1 and lower_counter >= 1 and upper_counter >= 1:
            print("Valid password of length {}".format(password_length))
            valid_counter = valid_counter + 1
        password_counter = password_counter + 1 
    else:  
        print("Invalid length")
        invalid_counter = invalid_counter + 1
        password_counter = password_counter + 1
    password_str = input("Enter a new password: ")


    
print("You tried {} passwords, {} valid, {} invalid".format(password_counter,valid_counter,invalid_counter))