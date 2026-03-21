""" #anagram using sorted function
s="listen"
t="silent"                       #using sorted function (very easy one)  O(1) i guessss
if sorted(s)==sorted(t):
    print("True")
else:
    print("False") 

s=str(input("Enter a string1:"))
t=str(input("Enter string 2:"))
if len(s)!=len(t):
    print("False")
    exit()
sdict={}                 #O(s+t) using hashmap , needs extra space thats it
tdict={}
for i in s:
    sdict[i]=sdict.get(i,0)+1
for i in t:
    tdict[i]=tdict.get(i,0)+1
print(sdict)
print(tdict)
if sdict==tdict:
    print("True")
else:
    print("False")

s=str(input("Enter a string1:"))
t=str(input("Enter string 2:"))
if len(s)!=len(t):
    print("False")
    exit()
sdict,tdict={},{}                 #  takes extra space complexity
for i in range(len(s)):
    sdict[s[i]]=1+sdict.get(s[i],0)
    tdict[t[i]]=1+tdict.get(t[i],0)
for c in sdict:
    if sdict[c]!=tdict.get(c,0):
        print("False")
        break
else:
    print("True")

#if we need to do it in O(1) space complexity we used sorted function but regarding time it takes O(n), O(log n) or sometimes O(1) depends on the sorting algo used
sorted(s)==sorted(t)
print("True")
"""

nums=[1,2,3,4,16,90,8,7,8,9,12,7]
target=7
found=False                                  #low=0, high=len(nums)-1 , while low<=high: loop repeats until the element is found or not. mid=(low+high)//2 and if nums[mid]==target: return nums[mid] elif nums[mid]>target high=mid-1  else low=mid+1   otherwise return -1
for i in range(len(nums)):
    if nums[i]==target:
        print(i)
        found=True
        break
if not found:
    print(-1)