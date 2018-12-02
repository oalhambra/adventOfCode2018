def toInt(str):
    return int(str)



f = open("../inputs/day1.txt", "r")
data=f.read()

# data=data.replace('+','')
data =data.split('\n')
data.pop()

data=list(map(int,data))

frecuency=0
frecuencyList=[0]
found=False
counter=0
while not found:
    # print(frecuency)
    for val in data:
        frecuency+=val
        # print(frecuency)
        if frecuency in frecuencyList:
            print(frecuency)
            found=True
            break
        frecuencyList.append(frecuency)


    counter+=1
    print(counter,frecuency)


