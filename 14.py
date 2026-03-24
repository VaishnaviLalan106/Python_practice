a=[1,2,3,4]
b=[3,4,5,6]
int1=set(a)
int2=set(b)
print([i for i in int1 if i in int2])

#anagrams
strs=["ate","listen","tan","nat","silent","eat","tea"]
group={}
for s in strs:
    key=''.join(sorted(s))
    if key in group:
        group[key].append(s)
    else:
        group[key]=[s]
print(group)
print(group.values()) 

a=[1,2,3,2,1]
b=[5,6,7,4]
print(a + b)
set1=set(a)
set2=set(b)
print(list(set1 | set2))
print(list(set1 - set2))
print(list(set1 ^ set2))

#palindrome
word="vaishu"
print(word)
palword=word[::-1]
print(palword)

#using loop to palindrome
word=str(input("Enter a word:"))
print(word)
list1=list(word)
print(list1)
list2=[]
for i in range(len(list1)):
    list2.append(list1[len(list1)-i-1])
print(list2)
if list1==list2:
    print("Palindrome")
else:
    print("Not a Palindrome")


