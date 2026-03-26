#division operatio n which takes O(n) tc which is simple but time taking
nums=[1,2,3,4]
answer=1
for i in nums:
    answer=answer*i
print(answer)
list1=[]
list1.append(answer//1)
list1.append(answer//2)
list1.append(answer//3)
list1.append(answer//4)
print(list1)