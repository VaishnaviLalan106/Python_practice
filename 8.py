
nums=list(map(int,input("Enter numbers(ur wish reyy):").split()))
print(nums)
print(max(nums))
print(min(nums))
store=[]
nums.remove(max(nums))
print(nums)
print(max(nums))
 
unique_nums = list(set(nums))
print("First largest number is:",max(nums))
found=False
for i in range(len(nums)):
    if max(unique_nums):
        temp=max(unique_nums)
        unique_nums.remove(temp)
        found=True
        break
    else:
        print("nothing")
print("second largest number is:",max(unique_nums)) 


nums=[1,2,3,4,4,6,7]
for i in range(len(nums)):
    if nums[i]==nums[i]:
        if nums[i]==nums[i+1]:
            print(f"{nums[i]} is repeated {nums.count(nums[i])} times")
        else:
            print(f"{nums[i]} is repeated one times")

from collections import defaultdict
nums=[1,2,2,3,4,4,5]
group=defaultdict()
for i in nums:
    group[i]=nums.count(i)
print(group)
for i in group:
    print(f"The number {i} is repeated {group[i]} times")

       

        