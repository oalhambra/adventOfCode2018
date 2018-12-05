with open("../inputs/day5.txt", "r") as f:
    data = f.read()

data = list(data.split("\n")[0])

types = set(map(str.lower, data))
lengths = []
for el in types:
    newData = []
    newData = list(filter(lambda a: a != el, data))
    newData = list(filter(lambda a: a != el.upper(), newData))
    i = 0
    while i < newData.__len__() - 1:
        if newData[i] != newData[i + 1] and newData[i].upper() == newData[i + 1].upper():
            newData.pop(i + 1)
            newData.pop(i)
            if i != 0:
                i -= 1
        else:
            i += 1
    lengths.append(newData.__len__())
print(min(lengths))
