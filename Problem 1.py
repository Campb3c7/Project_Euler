list = []
sum = 0

for i in range(1000):
    if ((i % 3) == 0 or (i % 5) == 0):
        list.append(i)
for i in range(len(list)):
    sum += list[i]

print(sum)


