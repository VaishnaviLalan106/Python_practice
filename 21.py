""" sent="abcabcbb"
print(sent)
sets=set(sent)
print(sets)                  #i tried to fin unique characters ,not the longest substring my mistake
curve=0
for i in range(len(sent)):
    if sent==sets:
        print(f"longest substring without repeating characters is {len(sets)}")
        break
    else:
        curve=curve+1
        print(f"longest substring without repeating characters is {len(sets)}")
        break 


sent="pwwkew"

longest=0
for i in range(len(sent)):
    seen=set()
    for j in range(i,len(sent)):
        if sent[j] in seen:
            break
        seen.add(sent[j])
    longest=max(longest,len(seen))
print(f"longest substring without repeating characters is {longest}")


word="abcbcbb"
seen=set()
left=0
longest=0

for right in range(len(word)):
    while word[right] in seen:
        seen.remove(word[left])
        left+=1

    seen.add(word[right])
    longest=max(longest,right-left+1)
print(f"longest substring without repeating characters is {longest}") 


nums = [2,1,5,1,3,2]
k=3

window_sums=sum(nums[:k])
max_sum=window_sums
print(window_sums)
print(max_sum)

for i in range(k,len(nums)):
    window_sums=window_sums-nums[i-k]+nums[i]
    max_sum=max(max_sum,window_sums)
print(max_sum)
 """

#two sums but not brute force
nums=[2,7,11,15]
k=9
target={}
for i in range (len(nums)):
    target[nums[i]]=i
print(target)
for i in range(len(nums)):
    diff=k-nums[i]
    if diff in target and target[diff]!=i:
        print([i,target[diff]])
        break