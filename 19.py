#longest consecutive sequence
unsortedarr=[76,9,8,8,0,3,4,23,1,5,3,5,7,6]
print(unsortedarr)
nums=sorted(set(unsortedarr))
print(nums)
arr=[nums[0]]
for i in range(0,len(nums)-1):
    if nums[i]+1==nums[i+1]:
        arr.append(nums[i+1])
print(arr)
print(len(arr))
