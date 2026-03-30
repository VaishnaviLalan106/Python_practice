""" #longest consecutive sequence
unsortedarr=[76,9,8,8,0,3,4,23,1,5,3,5,7,6]
print(unsortedarr)
nums=sorted(set(unsortedarr))
print(nums)
arr=[nums[0]]
for i in range(0,len(nums)-1):
    if nums[i]+1==nums[i+1]:
        arr.append(nums[i+1])
print(arr)
print(len(arr)) """


""" #longest word 
sent="I love: programming, so so much"
word=list(sent.split())
print(word)
longest=""
for i in range(len(word)):
    word[i]=word[i].strip(",:.")
    if len(word[i])>len(longest):
        longest=word[i]
print(longest,len(longest))
 """

#to count words
sent="hellllooo, there   how are     youuu??"
sent=sent.split()
print(sent)
count=0
for i in sent:
    clean=""
    for ch in i:
        if ch.isalpha():
            clean+=ch
    print(clean)
    if clean:
        count+=1
print(f"There are {count} words")
