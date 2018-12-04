def getFirst(pair):
    return pair[0]


with open("../inputs/day4.txt","r") as f:
    data=f.read()
# [1518-05-29 00:00] Guard #1151 begins shift
data=data.split("\n")
data.pop()

processedData=[]
for el in data:
    piece=el.split("]")
    piece[0]=piece[0].replace("[","")
    piece[0]=piece[0].replace("-","")
    piece[0]=piece[0].replace(":","")
    piece[0]=piece[0].replace(" ","")
    piece[0]=int(piece[0])

    if "#" in piece[1]:
        piece[1]=piece[1].split(" ")[2]
        piece[1]=int(piece[1].replace("#",""))

    processedData.append(piece)


processedData.sort(key=getFirst)
# print(processedData)

guards={}
currentGuard=-1
startDate=-1
asleepCounter=0
wakeUpCounter=0
for shift in processedData:
    # print(shift)
    if shift[1]!=' falls asleep' and shift[1]!=' wakes up':
        currentGuard=shift[1]
    elif shift[1]==' falls asleep':
        startDate=shift[0]
        asleepCounter+=1
    else:
        wakeUpCounter+=1
        time=shift[0]-startDate
        if currentGuard in guards:
            guards[currentGuard]+=time
        else:
            guards[currentGuard]=time

lazyGuard=max(guards, key=guards.get)
currentGuard=-1
minutes={}
for shift in processedData:
    print(shift)
    if shift[1]==lazyGuard:
        currentGuard=shift[1]
    elif shift[1]==' falls asleep' and currentGuard==lazyGuard:
        startDate=shift[0]
        asleepCounter+=1
    elif shift[1]==' wakes up' and currentGuard==lazyGuard:
        wakeUpCounter+=1
        for i in range(int(str(startDate)[8:]),int(str(shift[0])[8:])):
            if i in minutes:
                minutes[i]+=1
            else:
                minutes[i]=1
        # time=shift[0]-startDate

    else:
        currentGuard=-1

keyMinute=max(minutes, key=minutes.get)
print(lazyGuard,keyMinute,lazyGuard*keyMinute)


