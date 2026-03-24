a=[1,2,3,4]
b=[3,4,5,6]
int1=set(a)
int2=set(b)
print([i for i in int1 if i in int2])

#anagrams
strs=["ate","listen","tan","nat","silent","eat","tea"]
group={}
for s in strs:
    key=''.join(sorted(s))
    if key in group:
        group[key].append(s)
    else:
        group[key]=[s]
print(group)
print(group.values())