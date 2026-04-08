sets = input("Enter string: ")
print(sets)
setu=set()
found=False
for s in sets:
    if s in setu:
        print(f"{s} is first duplicate")
        found=True
        break
    else:
        setu.add(s)
if not found:
    print("no duplicate found")
        
#brute force approach for container with most water     
height=[1,8,6,2,5,4,8,3,7]
res=0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        area=min(height[i],height[j])*(j-i)         #O(n^2) brute force 
        res=max(res,area)
print(f"container with most water is {res}")

#two pointer approach for container with most water
height=[1,8,6,2,5,4,8,3,7]
l,r=0,len(height)-1
res=0
while l<r:
    area=min(height[l],height[r])*(r-l)         #O(n) two pointer approach 
    res=max(res,area)
    if height[l]>height[r]:
        r-=1
    else:
        l+=1
print(f"container with most water is {res}")

#trapping rain water 
height=[0,1,0,2,1,0,1,3,2,1,2,1]
res=0
lmax=[]
rmax=[]
for i in range(len(height)):
    lmax.append(max(height[:i+1]))
    rmax.append(max(height[i:]))
    print(lmax[:i+1])          #for my study purpose
    print(rmax[i:])
    res+=min(lmax[i],rmax[i])-height[i]
print(res)

#two pointer approach 
height=[0,1,0,2,1,0,1,3,2,1,2,1]
l,r=0,len(height)-1
res=0
lmax=height[l]
rmax=height[r]                      #it checks lmax and rmax at each step and calculates the area
while l<r:
    if lmax<rmax:
        l+=1
        lmax=max(lmax,height[l])       #it updates lmax and rmax at each step
        res+=lmax-height[l]              #it adds the area to the result
    else:
        r-=1
        rmax=max(rmax,height[r])
        res+=rmax-height[r]
print(res)


 #using o(n^2) approach like i checks from 0 index and j also check 0 index , so subarray will be 1 then j goes to 1 index then array will be 1+1 =2 then count =1 bec sum==k
nums=[1,1,1]
k=2
count=0
for i in range(len(nums)):
    sum=0
    for j in range(i,len(nums)):
        sum+=nums[j]
        #print(sum)
        if sum==k:
            count+=1
print(count)

#using hashmap and storing current prefix sum and checking if (current_sum - k) is present in hashmap
nums=[1,1,1]
k=2
hash={0:1}
current_sum=0
count=0
for i in range(len(nums)):
    current_sum+=nums[i]
    #print(sum)
    if current_sum-k in hash:
        count+=hash[current_sum-k]
    hash[current_sum]=hash.get(current_sum,0)+1         #using O(n) approach
print(count)
 
#longestsubarray
nums=[1,-1,5,-2,3]
k=3
maxs=0
for i in range(len(nums)):
    sum=0
    for j in range(i,len(nums)):
        sum+=nums[j]
        if sum==k:
            print(nums[i:j+1])
            maxs=max(maxs,j-i+1) 
print(maxs) 
#longest subarray with sum==k
nums=[1,-1,5,-2,3]
k=3
hash={0:-1}
curr_sum=0
maxs=0
for i in range(len(nums)):
    curr_sum+=nums[i]
    if curr_sum-k in hash:
        maxs=max(maxs,i-hash[curr_sum-k])
    if curr_sum not in hash:
        hash[curr_sum]=i
print(hash)
print(maxs)
