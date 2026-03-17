arr=[1,5,7,9,24]
print(arr)
print("right now length of list is:",len(arr))
k=int(input("enter the number insert:"))
for i in arr:
    if i==k:
        print(f"{k} is found")
        break
else:
    print(f"{k} not found")
    
k=int(input("enter the number insert:"))
print("the number is:",k)
while True:
     pos=int(input("enter the position to insert:"))
     if pos>len(arr):
         print("position is out of range")
     else:
         print("the position is:",pos)
         break
if k in arr:
         print(f"{k} is found")
else:
        arr.insert(pos,k)
        print(arr)
print("After inserting:",len(arr))

arr=[1,5,7,9,24]
print(arr)
for i in arr:
    print(i)
high=arr[len(arr)-1]
print("the highest element is:",high)
low=arr[0]
print("the lowest element is:",low)
mid=arr[len(arr)//2]
print("the middle element is:",mid)
k=7
if k==high:
    print(f"{k} is found")
elif k==low:
    print(f"{k} is found")
elif k==mid:
    print(f"{k} is found")
else:
    print(f"{k} not found")

num=int(input("enter the number:"))
def fact(hi):
    if hi<=1:
        return 1
    else:
        fact=1
        for i in range(1,hi+1):
            fact=fact*i
        return fact
print(fact(hi=num))
    
    