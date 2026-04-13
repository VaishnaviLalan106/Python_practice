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
            
