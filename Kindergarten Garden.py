# Given a diagram, determine which plants each child in the kindergarten class is responsible for.
#
# The kindergarten class is learning about growing plants. The teacher thought it would be a good idea to give them actual seeds, plant them in actual dirt, and grow actual plants.
#
# They've chosen to grow grass, clover, radishes, and violets.
#
# To this end, the children have put little cups along the window sills, and planted one type of plant in each cup, choosing randomly from the available types of seeds.
#
# [window][window][window]
# ........................ # each dot represents a cup
# ........................
# There are 12 children in the class:
#
# Alice, Bob, Charlie, David,
# Eve, Fred, Ginny, Harriet,
# Ileana, Joseph, Kincaid, and Larry.
# Each child gets 4 cups, two on each row. Their teacher assigns cups to the children alphabetically by their names.
#
# The following diagram represents Alice's plants:
#
# [window][window][window]
# VR......................
# RG......................
# In the first row, nearest the windows, she has a violet and a radish. In the second row she has a radish and some grass.
#
# Your program will be given the plants from left-to-right starting with the row nearest the windows. From this, it should be able to determine which plants belong to each student.
#
# For example, if it's told that the garden looks like so:
#
# [window][window][window]
# VRCGVVRVCGGCCGVRGCVCGCGV
# VRCCCGCRRGVCGCRVVCVGCGCV
# Then if asked for Alice's plants, it should provide:
#
# Violets, radishes, violets, radishes
# While asking for Bob's plants would yield:
#
# Clover, grass, clover, clover
# --------------------------------------------------------------------------------------------------

first_row = "VRCGVVRVCGGCCGVRGCVCGCGV"
second_row = "VRCCCGCRRGVCGCRVVCVGCGCV"

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
def rows_to_words(row):
    list = []
    for letter in row:
        if letter == "V":
            list.append("violets")
        elif letter == "R":
            list.append("radishes")
        elif letter == "C":
            list.append("clover")
        else:
            list.append("grass")
    return list

def who_took_what (name):
    number = names.index(name)
    print (f"{name} took {list_one[number*2].capitalize()}, {list_one[(number*2)+1]}, {list_two[number*2]} and {list_two[(number*2)+1]}")

list_one = rows_to_words(first_row)
list_two = rows_to_words(second_row)
who_took_what("Alice")
who_took_what("Bob")
who_took_what("Charlie")
who_took_what("Larry")