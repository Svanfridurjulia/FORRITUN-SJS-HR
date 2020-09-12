dog_age = int(input("Input dog's age: ")) # Do not change this line

human = 16


if 0 < dog_age < 17:
    human_count = dog_age * human - (dog_age*dog_age*dog_age)
    print("Human age:", int(human_count))
else:
    print("Invalid age")



if 1 < dog_age < 17:
    human_age = human + dog_age * 4 + 1
    print("Human age:", human_age)
elif dog_age == 1:
    print("Human age:", human)
else:
    print("Invalid age")

#1.User input
#2.Create one variable outside the if statement
    #2a. One variable for the starting human age
#3.Use if statement for when the dog_age is more than 1 but less than 17
    #3a. calculate the human age
#4.Use elif statement for when the dog_age is equal to 1
    #4a.The calculations work after dog_age = 2
#5.Else is for when the dog_age is less than 0 

