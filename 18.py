#encode
word="Hello, World!!"
strs=word.split(" ")
print(strs)
res=""
for s in strs:
    res+=str(len(s))+ "#" + s
print(res)

#decode
strs=res
res,i=[],0

while i < len(strs):
    j=i
    while strs[j]!="#":
        j+=1
    length=int(strs[i:j])
    res.append(strs[j+1:j+1+length])
    i=j+1+length
print(res)

#second largest
nums=list(map(int,input("Enter the numbers separated by space:").split()))
nums=list(set(nums))
print(nums)
max1=nums[0]
for i in range(len(nums)):
    if nums[i]>max1:
        max1=nums[i]
print(max1)
nums.remove(max1)
print(nums)
max2=nums[0]
for i in range(len(nums)):
    if nums[i]>max2:
        max2=nums[i]
print(max2)

#add pairss to get sum
nums=[2,3,4,5,6,7,8]
target=7                                     #brute force approach
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(f"{nums[i]}+{nums[j]}={target}")
        break

#other logic
nums=list(map(int,input("Enter the numbers separated by space:").split()))
target=int(input("Enter the target sum:"))
seen=set()
pairs=[]
for i in nums:
    needed=target-i
    if needed in seen:
        pairs.append((needed,i))
    seen.add(i)
pairs.sort()
print(pairs)
