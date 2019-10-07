user_input = int(input("Enter number that you want to divide: "))
list_of_numbers = []

for i in range(1,user_input+1):
    if user_input % i == 0:
        list_of_numbers.append(i)
print(list_of_numbers)