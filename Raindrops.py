def raindrops(number):
    output = ""
    if number%3 == 0:
        output += "Pling"
    if number%5 == 0:
        output += "Plang"
    if number%7 == 0:
        output += "Plong"
    else:
        output = f"{number}"
    return output

print(raindrops(35))