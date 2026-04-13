#buy and sell stock
input=[7,1,5,3,6,4]
l=0  #left=buy
r=1  #right=sell
max_profit=0
while r<len(input):
    #profitable?
    if input[l]<input[r]:
        profit=input[r]-input[l]
        max_profit=max(max_profit,profit)
    else:
        l=r
    r+=1
print(max_profit)

nums = [4, 2, -3, 1, 6]
for i in range(len(nums)):
    curr_sum=0
    for j in range(i, len(nums)):
        curr_sum+=nums[j]
        if curr_sum==0:
            print(nums[i:j+1])
            

#prefix map+hashmap
nums = [4, 2, -3, 1, 6]
prefix_map={}
curr_sum=0
for i in range(len(nums)):
    curr_sum+=nums[i]

    #if prefix sum is 0
    if curr_sum==0:
        print(nums[0:i+1])

    #if prefix sum seen before
    if curr_sum in prefix_map:
        for prev_index in prefix_map[curr_sum]:
            print(nums[prev_index+1:i+1])
    
    if curr_sum in prefix_map:
        prefix_map[curr_sum].append(i)
    else:
        prefix_map[curr_sum]=[i]
print(curr_sum)
print(prefix_map)