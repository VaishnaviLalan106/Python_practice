#brute force approach we all use normally
nums=[-3,3,4,-3,1,2]
target=0
set=set()
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                set.add((nums[i],nums[j],nums[k]))
print(set)

#my code later modified by adding
srt=sorted(nums)
l,r=0,len(nums)-1
orgset=[]
for i in range(len(nums)):
    if i>0 and srt[i]==srt[i-1]:
        continue
    while l<r:
        current=srt[i]+srt[l]+srt[r]
        if current==target:
            orgset.append([srt[i],srt[l],srt[r]])
            l+=1
            while l<r and srt[l]==srt[l-1]:
                l+=1
            r-=1
        elif current<target:
            l+=1
        else:
            r-=1
print(orgset)  

#the one neetcode bhai taught seeing this modified
res=[]
nums.sort()
for i in range(len(nums)):
    if i>0 and nums[i]==nums[i-1]:
        continue
    l,r=i+1,len(nums)-1
    while l<r:
        threesum=nums[i]+nums[l]+nums[r]
        if threesum>target:
            r-=1
        elif threesum<target:
            l+=1
        else:
            res.append([nums[i],nums[l],nums[r]])
            l+=1
            while l<r and nums[l]==nums[l-1]:
                l+=1
print(res)