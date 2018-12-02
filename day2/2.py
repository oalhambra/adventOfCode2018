
with open("../inputs/day2.txt","r") as f:
    data=f.read()
data=data.split("\n")
data.pop()

while data !=[]:
    word1=data.pop()
    for word2 in data:
        different=0
        matching=''
        for i in range(word1.__len__()):
            if word1[i] != word2[i]:
                different+=1
            else:
                matching+=word2[i]
            if different==2:
                break
        if different==1:
            print(matching)
            break
