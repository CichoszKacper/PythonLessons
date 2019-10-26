def high_scores(list):
    return list[len(list)-1]
def high_scores(list):
    list.sort()
    return list[len(list)-1]
def second_highest(list):
    list.sort()
    return list[len(list)-2]
def third_highest(list):
    list.sort()
    return list[len(list)-3]

list = [20,30,50,40,22,33,52,21,40]
print(list[len(list)-1])
print(high_scores(list))
print(second_highest(list))
print(third_highest(list))
