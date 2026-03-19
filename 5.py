num=[1,2,3,4,5]
print(num[2])
num.extend([9,28,348])
print(num[6])
extra=5*len(num) #wanted to resize array but couldnt 
print(extra)
num[0]=99
print(num)
print(len(num))
#print(num[10])  index out of range 
num.remove(5)     #deletion of element 
num.insert(0,30)   #adding element into index before it 
print(num)