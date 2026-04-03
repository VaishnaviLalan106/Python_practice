#remove duplicates in original list without changing order
nums = [1,1,2,2,3,4,4]
l=1
for i in range(1,len(nums)):
    if nums[i]!=nums[i-1]:
        nums[l]=nums[i]
        l+=1
print(l)
print(nums[:l])

#container with most water using two pointers having area already fixed.
height = [1,8,6,2,5,4,8,3,7]
l,r=0,len(height)-1
maxarea=0
while l<r:
     max_area=min(height[l],height[r])*(r-l)
     if max_area>maxarea:
        maxarea=max_area
     if height[l]>height[r]:
        r-=1
     else:
        l+=1
print(f"Container with most water is {maxarea}")
    

#longest subarray with sum<=k
nums = [2,1,5,1,3,2]
k = 7
l=0
sum=0
max_len=0
best=[]
for r in range(len(nums)):
    sum+=nums[r]
    while sum>k:
        sum-=nums[l]
        l+=1
    if r-l+1>max_len:
        max_len=r-l+1
        best=nums[l:r+1]
print(max_len)
print(best)


#check if str contains permutation of another
s1 = "ab"
s2 = "eidbaooo"
l=0
for i in range(len(s2) - len(s1) + 1):
    sub = s2[i:i+len(s1)]
    print(sub)
    found=False
    if sorted(s1)==sorted(sub):
        found=True
        print(True)
        break
if found:
    print("Permutation found")
else:
    print("Permutation not found")
print(s2[i:i+len(s1)])


#window means slicing of bigg arrays into smallers one and then checking use slices [i:j] or [:i] or [:j] for better understanding of slices. And for duplicates use set or sort and check. And for sum use sliding window technique. And for two pointers use l,r=0,len(nums)-1 and while l<r. And for checking if element is present in array use set or sort and check.