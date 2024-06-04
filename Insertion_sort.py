l=[10,20,3,40,6,50]
# //insertion sort 

for i in range(1,len(l)):
    key=l[i]
    
    j=i-1

    while j>=0 and key<l[j]:
        l[j+1]=l[j]         
        j=j-1
    l[j+1]=key
print(l)