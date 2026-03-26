""" """ #division operatio n which takes O(n) tc which is simple but time taking
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


#reducetime complexity in O(n) and easy way to get this ARYGH
nums=[1,2,3,4]
res=[1]*(len(nums))
prefix=1
for i in range(len(nums)):
    res[i]=prefix
    prefix*=nums[i]
print(prefix)
suffix=1
for i in range(len(nums)-1,-1,-1):
    res[i]*=suffix
    suffix*=nums[i]
print(suffix)
print(res)


#remove duplicate in string this is using logic
word=str(input("enter the string")).strip().lower()
seen=""
for ch in word:
    if ch not in seen:
        seen+=ch
print(seen)

#set looksup faster and is O(n) tc for longer strings
word=str(input("enter the string")).strip().lower()
seen=set()
res=""
for ch in word:
    if ch.isalpha() and ch not in seen:
        seen.add(ch)
        res+=ch
print(res)

#repeated characters in string
word = "vaishu"
print("original string",word)
seen=set(word)           # converted into set for easy lookup
print("in set",seen)
rep={}
for i in seen:
    if i in rep:
        rep[i]+=1
    else:
        rep[i]=1
print(rep)
for key,value in rep.items():
    print(f"{key}:{value}") 

word =str(input("enter the string")).strip().lower()
print("original string",word)
rep={}
for i in word:
    if i.isalpha():
        if i in rep:
            rep[i]+=1
        else:
            rep[i]=1
print(rep)
for key,value in rep.items():
    print(f"{key}:{value}")
max_count=max(rep.values())
for key,value in rep.items():
    if value==max_count:
        print(f"{key} value repeated {max_count} times")

