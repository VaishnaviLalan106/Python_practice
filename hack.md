
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
3. Given a string containing letters, digits, and symbols, determine if it reads the same forwards and backwards when considering only alphabetic characters (case-insensitive).

```python 
def isAlphabeticPalindrome(code):
    letter=[]
    for ch in code:
        if ch.isalpha():
            letter.append(ch)
    letter=[ch.lower() for ch in letter]
    if not letter:
        return 1
    elif letter==letter[::-1]:
        return 1
    else:
        return 0
```
3. Check for Non-Identical String Rotation
Given two strings s1 and s2, return 1 if s2 is a rotation of s1 but not identical to s1, otherwise return 0. 

```python 

def isNonTrivialRotation(s1, s2):
    if len(s1)!=len(s2):
        return False
    if s1!=s2 and s2 in s1+s1:
        return True
    else:
        return False 
```
3. Target Index Search
Given a sorted array of distinct integers and a target value, return the index of the target or -1 if not found.

```python

def binarySearch(nums, target):
    low=0
    high=(len(nums)-1)
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1
```

4. Find First Occurrence
Given a sorted array of integers that may contain duplicates, return the index of the first occurrence of a target value or -1 if not found.

```python

def findFirstOccurrence(nums, target):
    low=0
    high=(len(nums)-1)
    result=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            result=mid
            high=mid-1
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return result
```
4. Maximum Number of Non-Overlapping Intervals
Given an array of intervals where each interval has a start and end time, return the maximum number of non-overlapping intervals.

```python
def maximizeNonOverlappingMeetings(meetings):
    meetings.sort(key=lambda x:x[1])
    count=0
    last_end=float('-inf')
    for start,finish in meetings:
        if start>=last_end:
            count+=1
            last_end=finish
    return count
```

5. Validate Properly Nested Brackets
Given a string, check if all brackets ('()', '{}', '[]') are properly matched and nested. Return 1 if valid, otherwise return 0.

```python
def areBracketsProperlyMatched(code_snippet):
    stack=[]
    pairs={')':'(',']':'[','}':'{'}
    for ch in code_snippet:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1]!=pairs[ch]:
                return 0
            stack.pop()
    return 1 if not stack else 0
```
