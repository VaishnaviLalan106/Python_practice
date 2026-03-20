""" class myArray:
    def __init__(self,totalsize,usedsize):
        self.totalsize=totalsize
        self.usedsize=usedsize
        self.ptr=[0]*totalsize
    def set_values(self):
        for i in range(self.usedsize):
            num=int(input("enter the number:\n"))
            self.ptr[i]=num
    def show_values(self):
        print(self.ptr[:self.usedsize])

marks=myArray(10,5)
marks.set_values()
marks.show_values() """

nums=list(map(int,input("enter the numbers:").split()))    #using O(n^2) tc using normal arrays
found=False
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            print("True")
            found=True
            break
if not found:
    print("False")

nums=[1,2,3,4,5,1]
hashset=set()             #using hashset O(n) tc 
found=False
for i in range(len(nums)):
    if nums[i] in hashset:
        print("True")
        found=True
        break
    else:
        hashset.add(nums[i])
if not found:
    print("False")
print(hashset)
