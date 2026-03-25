arr=[1,1,2,2,3,4]
k=2
group={}
for i in arr:
    if i in group:
        group[i]+=1
    else:
        group[i]=1
print(group)
for key,values in group.items():
    if values==k:
        print([key])