def toInt(str):
    return int(str)



f = open("../inputs/day1.txt", "r")
data=f.read()

data=data.replace('+','')
data =data.split('\n')
data.pop()

data=map(toInt,data)

print(sum(data))
