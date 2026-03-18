
1. Count Elements Greater Than Previous Average
Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.

```python
def countResponseTimeRegressions(responseTimes):
    if len(responseTimes)<=1:
        return 0
    count=0
    for i in range(1,len(responseTimes)):
        previous_elements=responseTimes[:i]
        average=sum(previous_elements)/len(previous_elements)
        if responseTimes[i]>average:
            count+=1
    return count

```
2. Find the Smallest Missing Positive Integer
Given an unsorted array of integers, find the smallest positive integer not present in the array in O(n) time and O(1) extra space.

```python 
def findSmallestMissingPositive(orderNumbers):
    n = len(orderNumbers)
    contains_one = False
    for i in range(n):
        if orderNumbers[i] == 1:
            contains_one = True
        if orderNumbers[i] <= 0 or orderNumbers[i] > n:
            orderNumbers[i] = 1
    if not contains_one:
        return 1
    for i in range(n):
        idx = abs(orderNumbers[i])
        if 1 <= idx <= n:
            if orderNumbers[idx - 1] > 0:
                orderNumbers[idx - 1] *= -1
    for i in range(n):
        if orderNumbers[i] > 0:
            return i + 1
    return n + 1
```
