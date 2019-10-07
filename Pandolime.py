user_string = input("Please enter some word to check if it is pandolime: ")
user_string = user_string.lower()

if user_string[::] == user_string[::-1]:
    print("Your word is pandolime")
else:
    print("its not pandolime")