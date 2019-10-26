one_point = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
two_point = ["D", "G"]
three_point = ["B","C", "M", "P"]
four_point = ["F", "H", "V", "W", "Y"]
five_point = ["K"]
eight_point = ["J", "X"]
ten_point = ["Q", "Z"]

def calculate (word):
    word = word.upper()
    counter = 0
    for x in word:
        if x in one_point:
            counter+=1
        if x in two_point:
            counter+=2
        if x in three_point:
            counter+=3
        if x in four_point:
            counter+=4
        if x in five_point:
            counter+=5
        if x in eight_point:
            counter+=8
        if x in ten_point:
            counter+=10
    return counter
print(calculate("cabbage porno"))