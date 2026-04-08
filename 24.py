sets = input("Enter string: ")
print(sets)
setu=set()
found=False
for s in sets:
    if s in setu:
        print(f"{s} is first duplicate")
        found=True
        break
    else:
        setu.add(s)
if not found:
    print("no duplicate found")
        
#brute force approach for container with most water     
height=[1,8,6,2,5,4,8,3,7]
res=0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        area=min(height[i],height[j])*(j-i)         #O(n^2) brute force 
        res=max(res,area)
print(f"container with most water is {res}")

#two pointer approach for container with most water
height=[1,8,6,2,5,4,8,3,7]
l,r=0,len(height)-1
res=0
while l<r:
    area=min(height[l],height[r])*(r-l)         #O(n) two pointer approach 
    res=max(res,area)
    if height[l]>height[r]:
        r-=1
    else:
        l+=1
print(f"container with most water is {res}")


#trapping rain water 
height=[0,1,0,2,1,0,1,3,2,1,2,1]
res=0
for i in range(len(height)):
    lmax=0
    rmax=0
    for j in range(i):
        lmax=max(lmax,height[j])
    for j in range(i+1,len(height)):
        rmax=max(rmax,height[j])
    res+=min(lmax,rmax)-height[i]
print(res)