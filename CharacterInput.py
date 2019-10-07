name = input("Enter your name: ")
age = int(input("Enter your age: "))
hundred = str(2019 + (100-age))
r = int(input("Enter number of copies: "))
for i in range(r):
    print("Hello " + name + ". You will turn 100 years in " + hundred)