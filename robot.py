n=int(input("Quanti spostamenti?\n"))
p=[]
finalp=[]
for i in range(n):
    p=finalp
    finalp=[]
    if (i==0):
        finalp.append([-1,0,1])
        finalp.append([0,1,2])
        finalp.append([1,0,3])
        finalp.append([0,-1,4])
    else:
        for j in range(len(p)):
            if (p[j][2]==1 or p[j][2]==3):
                finalp.append([p[j][0],p[j][1]+1,2])
                finalp.append([p[j][0],p[j][1]-1,4])
            else:
                finalp.append([p[j][0]+1,p[j][1],1])
                finalp.append([p[j][0]-1,p[j][1],3])
if (n>1):
    for j in range(len(finalp)):
        for k in range(j+1,len(finalp)):
            if (finalp[j][0]==finalp[k][0] and finalp[j][1]==finalp[k][1]):
                finalp[k][2]=5
    truep=[]
    count=0
    for i in range(len(finalp)):
        if (finalp[i][2]!=5):
            truep += [finalp[i]]
            count += 1
print("Le possibili posizioni sono: ",count)
for i in range(len(truep)):
    print("({}:{}) ".format(truep[i][0],truep[i][1]))
