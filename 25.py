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

