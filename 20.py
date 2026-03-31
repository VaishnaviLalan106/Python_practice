s="a man, a plan, a canal: panama"
word=s.strip().lower()
print(word)
clean=""
for ch in word:
    if ch.isalpha():
        clean+=ch
print(clean)
found = True
for i in range(len(clean)//2):
    if clean[i]!=clean[len(clean)-i-1]:
        print("not a palindrome")
        found = False
        break
if found:
    print("a palindrome")
        