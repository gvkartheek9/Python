l=[15246,63214,95014,65123,56021]
l1=[]
res=[]
result=[]
tres=[]
d={}
for i in range(0,len(l)):
    val=str(l[i])
    l1.append(int(val[2]))
for i in range(0,len(l1)):
    res.append(l1[i])
res.sort()
print(l1)
for i in range(0,len(l)):
    d[l[i]]=l1[i]
for i in range(0,len(l1)):
    if(res.count(res[i])>1):
        repeated=[]
        value=[k for k,v in d.items() if v==res[i]]
        for i in range(0,len(value)):
            repeated.append(value[i])
        repeated.sort()
        for i in range(0,len(repeated)):
            tres.append(repeated[i])
    else:
        index=l1.index(res[i])
        tres.append(l[index])
print(tres)
for i in range(0,len(tres)):
    if(tres[i] not in result):
        result.append(tres[i])
        #print("kk")
    else:
        pass
print(result)
