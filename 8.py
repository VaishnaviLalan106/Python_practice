
nums=list(map(int,input("Enter numbers(ur wish reyy):").split()))
print(nums)
""" print(max(nums))
print(min(nums))
store=[]
nums.remove(max(nums))
print(nums)
print(max(nums))
 """
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