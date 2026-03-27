""" import collections
from collections import defaultdict
#invalid sudoku
sudoku_board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(sudoku_board)
cols=collections.defaultdict(set)
rows=collections.defaultdict(set)
squares=collections.defaultdict(set)
for r in range(9):
    for c in range(9):
        if sudoku_board[r][c]==0:
            continue
        if sudoku_board[r][c] in rows[r] or sudoku_board[r][c] in cols[c] or sudoku_board[r][c] in squares[(r//3,c//3)]:
            print(False)
            break
        cols[c].add(sudoku_board[r][c])
        rows[r].add(sudoku_board[r][c])
        squares[(r//3,c//3)].add(sudoku_board[r][c])
    else:
        continue
    break
else:
    print(True)


#valid sudoku
import collections
import collections
from collections import defaultdict
sudoku_board = [
    [7, 9, 2, 1, 5, 4, 3, 8, 6],
    [6, 4, 3, 8, 2, 7, 1, 5, 9],
    [8, 5, 1, 3, 9, 6, 7, 2, 4],
    [2, 6, 5, 9, 7, 3, 8, 4, 1],
    [4, 8, 9, 5, 6, 1, 2, 7, 3],
    [3, 1, 7, 4, 8, 2, 9, 6, 5],
    [1, 3, 6, 7, 4, 8, 5, 9, 2],
    [9, 7, 4, 2, 1, 5, 6, 3, 8],
    [5, 2, 8, 6, 3, 9, 4, 1, 7]
]
print(sudoku_board)
cols=collections.defaultdict(set)
rows=collections.defaultdict(set)
squares=collections.defaultdict(set)
for r in range(9):
    for c in range(9):
        if sudoku_board[r][c]==0:
            continue
        if sudoku_board[r][c] in rows[r] or sudoku_board[r][c] in cols[c] or sudoku_board[r][c] in squares[(r//3,c//3)]:
            print(False)
            break
        cols[c].add(sudoku_board[r][c])
        rows[r].add(sudoku_board[r][c])
        squares[(r//3,c//3)].add(sudoku_board[r][c])
    else:
        continue
    break
else:
    print(True)
 """

""" #to check if two strings are anagrams  
word1=str(input("Enter a word:")).lower().strip()
word2=str(input("Enter a word:")).lower().strip()
for ch in word1:
    if ch in word2 and len(word1)==len(word2):  # here we only checked character existence not anagarms 
        print("Anagrams")
        break
    else:
        print("Not Anagrams")
        break """

""" #to properly check anagrams we need to do this
word1=str(input("Enter a word:")).lower().replace(" ","")
word2=str(input("Enter a word:")).lower().replace(" ","")
core1={}
core2={}
for i in word1:
    core1[i]=core1.get(i,0)+1
for i in word2:
    core2[i]=core2.get(i,0)+1
print(core1)
print(core2)
if core1==core2:
    print("Anagrams")
else:
    print("Not Anagrams") """

""" #first non-repeated character
str=str(input("Enter a string:")).lower().strip()
count={}
for i in str:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
found=False
for i in str:
    if count[i]==1:
        print(f"{i} is the first non-repeated character")
        found=True
        break 
if not found:
    print("No non-repeated character found") """

"""other way is 
for key,values in count.items():
    if values==1:
        print(f"{key} is the first non-repeated character")
        break """
#type 1
word1="a man, a plan, a canal:panama"
word1=word1.lower().replace(" ","").replace(",","").replace(":","")
if word1.isalpha() and word1==word1[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

#type 2
word1=input("Enter a word:").lower().strip()
clean=""
for ch in word1:
    if ch.isalpha():
        clean+=ch
print(clean)
found=False
for i in range(len(clean)):
    if clean[i]==clean[len(clean)-i-1]:
        found=True
        print("Palindrome")
        break
if not found:
    print("Not a Palindrome")
        