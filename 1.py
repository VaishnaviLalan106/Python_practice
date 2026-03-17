num=0
store=[]
for i in range(5):
    num=int(input("enter the number:"))
    print("the number is:",num)
    store.append(num)
    print(store)    
yes=sorted(store)
print("the sorted list is:",yes)
print(max(store))
print(min(store))
sum=0
for i in store:
    sum+=i
print("the sum of the list is:",sum)
avg=sum/len(store)
print("the average of the list is:",avg)
for i in store:
    if i>avg:
        print("the numbers greater than average are:",i)