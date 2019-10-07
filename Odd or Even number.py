number = int(input("Enter number: "))
divider = int(input("Enter you divider: "))

if number % divider ==0:
    print("Your number " + str(number) + " is dividable by " + str(divider))
else:
    print ("Your number " + str (number) + " is not dividable by " + str (divider))