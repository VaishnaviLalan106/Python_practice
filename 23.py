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
     elif height[l]>height[r]:
        r-=1
     else:
        l+=1
print(f"Container with most water is {maxarea}")
    