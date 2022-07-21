def insrt(nlist):
    for pnum in range(len(nlist)-1,0,-1):
        for i in range(pnum):
            while nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
nlist=[28,34,56,72,86,42]
insrt(nlist)
print(nlist)
