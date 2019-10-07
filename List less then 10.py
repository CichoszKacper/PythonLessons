a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_input = int(input("Enter your number: "))

print([i for i in a if i < user_input])
