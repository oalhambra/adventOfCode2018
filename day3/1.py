
with open("../inputs/day3.txt","r") as f:
    data=f.read()
data=data.split("\n")
data.pop()
#1 @ 509,796: 18x15
dataProcessed=[]

for elem in data:
    aux1=elem.split(" ")
    aux1[0]=aux1[0].replace("#","")
    aux2=aux1[2].split(",")
    aux2[1]=aux2[1].replace(":","")
    aux3=aux1[3].split("x")
    dataProcessed.append([aux1[0],aux2[0],aux2[1],aux3[0],aux3[1]])


fabric=[]
for i in range(1000):
    aux=[]
    for j in range(1000):
        aux.append(0)
    fabric.append(aux)
counter=0
print(dataProcessed)

for elem in dataProcessed:
    for i in range(int(elem[3])):
        for j in range(int(elem[4])):
            if fabric[int(elem[1])+i][int(elem[2])+j]==0:
                fabric[int(elem[1])+i][int(elem[2])+j]=int(elem[0])
            else:
                fabric[int(elem[1])+i][int(elem[2])+j]=-1

for i in range(1000):
    for j in range(1000):
        if fabric[i][j]==-1:
            counter+=1


print(counter)


