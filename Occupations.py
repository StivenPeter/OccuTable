
occDict = {}

def OccPrep(): 
    occ = open("occupations.csv","r")
    ZeList = []
    occ.next()
    for row in occ:
        ZeList.append(row)
    for i in ZeList:
        d = i.rfind(",")
        occDict[i[0:d]] = float(i[d+1:len(i)])
    del occDict['Total']

def randOcc():
    from random import randint
    p = randint(0,1000)
    t = 0
    for key in occDict:
        t += occDict[key]
        if (t * 10) >= p:
            return key

