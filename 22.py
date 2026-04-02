nums=[0,-1,1,2,-1,-4]
target=0
""" set=set()
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                set.add((nums[i],nums[j],nums[k]))
print(set)
 """

l,r=0,len(nums)-1
orgset=set()
while l<r:
    current=nums[l]+nums[r]
    if current==target:
        orgset.add((nums[l],nums[r]))
        l+=1
        r-=1
    elif current<target:
        l+=1
    else:
        r-=1
print(orgset)