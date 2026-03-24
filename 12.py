nums=list(map(int,input("Enter numbers:").split()))
print("input list is:", nums)
print(len(nums))
k=int(input("Enter target sum:"))
print(f"k={k}")
sort=sorted(nums)
print("sorted list is:", sort)
k=int(input("Enter target sum:"))
print(f"k={k}")                 
found=False
for i in range(len(sort)):           #brute force O(n^2) time complexity
    for j in range(i+1,len(sort)):
        if sort[i]+sort[j]==k :
            print([i,j])
            found=True
            break
if not found:
    print("bye") 


hash={}                  #using O(n) time complexity 
for i , values in enumerate(nums):
      diff=k-values
      if diff in hash:
        print([hash[diff],i])
      hash[values]=i 

