nums=[1,2,2,3,5,5,5,7,3,8,1,2,8]
group={}
for i in nums:
    if i in group:
        group[i]+=1
    else:
        group[i]=1
print(group)
for key,values in group.items():
    print(f"{key} is repeated {values} times")
maximum_count=max(group,key=group.get)
print(f"{maximum_count} is repeated the most {group[maximum_count]} times")
for key,values in group.items():
    if key==maximum_count:
        temp=group[key]
        del group[key]
        break
second_max=max(group,key=group.get)
print(f"{second_max} is repeated the second most {group[second_max]} times")
minimum_count=min(group,key=group.get)
print(f"{minimum_count} is repeated the least {group[minimum_count]} times")
print(group)


#by doing this it deletes original copy og dictionary so we used to copy data
group={1: 2, 2: 3, 3: 2, 5: 3, 7: 1, 8: 2}
maximum_count=max(group,key=group.get)
print(f"{maximum_count} is repeated the most {group[maximum_count]} times")
for key,values in group.items():
    if key==maximum_count:
        temp=group.copy()
        del temp[maximum_count]
        break
second_max=max(temp,key=temp.get)
print(f"{second_max} is repeated the second most {temp[second_max]} times")
print(group)


#IF BOTH VALUES HAS SAME COUNT
max_count=max(group.values())
print(max_count)
for key,values in group.items():
    if values==max_count:
        print(f"{key} is repeated {values} times")