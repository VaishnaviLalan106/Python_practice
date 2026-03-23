nums=list(map(int,input("Enter numbers:").split()))
print("input list is:", nums)
print(len(nums))
k=int(input("Enter target sum:"))
print(f"k={k}")
found=False
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==k :
            print([i,j])
            found=True
            break
if not found:
    print("bye")

        

