with open("../inputs/day5.txt","r") as f:
    data=f.read()

data=list(data.split("\n")[0])
i=0

print(data.__len__())
while i<data.__len__()-1:
    if data[i]!=data[i+1] and data[i].upper()==data[i+1].upper():
        data.pop(i+1)
        data.pop(i)
        if i!=0:
            i-=1
    else:
        i+=1
print(data.__len__())