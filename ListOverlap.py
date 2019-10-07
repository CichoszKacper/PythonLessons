import random

a = [random.randint(0, 20) for i in range(10)]
print(a)
b = [random.randint(0, 20) for i in range(10)]
print(b)

c = []

for i in a:
    if i in a and i in b:
        c.append(i)

c = list(dict.fromkeys(c))
print(c)