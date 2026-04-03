nums = [1,1,2,2,3,4,4]
l=1
for i in range(1,len(nums)):
    if nums[i]!=nums[i-1]:
        nums[l]=nums[i]
        l+=1
print(l)
print(nums[:l])