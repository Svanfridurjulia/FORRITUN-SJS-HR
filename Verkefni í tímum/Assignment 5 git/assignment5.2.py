
n = int(input("Enter the length of the sequence: ")) # Do not change this line
count_1 = 1
count_2 = 2
count_3 = 3

print(count_1)
print(count_2)
print(count_3)

for n in range(n-3):
    sum = count_1 + count_2 + count_3
    count_1 = count_2
    count_2 = count_3
    count_3 = sum
    print(sum)
