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

#to check if two strings are anagrams
word1=str(input("Enter a word:")).lower().strip()
word2=str(input("Enter a word:")).lower().strip()
for ch in word1:
    if ch in word2 and len(word1)==len(word2):
        print("Anagrams")
        break
    else:
        print("Not Anagrams")
        break