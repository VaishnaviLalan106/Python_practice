arr=[1,1,1,2,2,3,4]
k=2
group={}             # as this is true but sorted takes O(nlogn) tc 
for i in arr:
    if i in group:
        group[i]+=1
    else:
        group[i]=1
print(group)
for key,values in group.items():
    if values>1:
        print([key]) 
        
#for top k most frequent element use bucket sort  O(n)
arr=[1,1,1,2,2,3,4]
k=2
group={} 
for i in arr:
    group[i]=group.get(i,0)+1
print(group)
bucket=[[] for i in range(len(arr)+1)]
for key, values in group.items():
    bucket[values].append(key)
print(bucket)
result=[]
for i in range(len(bucket)-1,0,-1):
    for i in bucket[i]:
        result.append(i)
        if len(result)==k:
            print(result)