
nums=list(map(int,input("Enter numbers(ur wish reyy):").split()))
print(nums)
print(max(nums))
print(min(nums))
 
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

""" 
#   WRONG APPROACH 
nums=[1,2,3,4,4,6,7]
for i in range(len(nums)):
    if nums[i]==nums[i+1]:                    #index out of range 
        print(f"{nums[i]} is repeated {nums.count(nums[i])} times")
    else:
        print(f"{nums[i]} is repeated one times") """

from collections import defaultdict
nums=[1,2,2,3,4,4,5]
group=defaultdict()
for i in nums:
    group[i]=nums.count(i)    # O(n^2) for large data 
print(group)
for i in group:
    print(f"The number {i} is repeated {group[i]} times")

#so for better approach O(n)
just={}
for i in nums:
    if i in just:
        just[i]+=1
    else:
        just[i]=1
for i in just:
    print(f"{i} repeated {just[i]} times")

       

        