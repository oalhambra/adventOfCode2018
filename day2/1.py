
with open("../inputs/day2.txt","r") as f:
    data=f.read()
data=data.split("\n")
data.pop()
doubleLetter=0
trippleLetter=0
for word in data:
    aDict = dict(zip('abcdefghijklmnopqrstuvwxyz', [0]*27))
    for letter in word:
        aDict[letter]+=1
    if 2 in aDict.values():
        doubleLetter+=1
    if 3 in aDict.values():
        trippleLetter+=1

print(doubleLetter*trippleLetter)