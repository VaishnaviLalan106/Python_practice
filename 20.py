""" s="a man, a plan, a canal: panama"
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
    print("a palindrome") """

#rotation
s1=str(input("enter the string1:")).strip().lower()
s2=str(input("enter the string2:")).strip().lower()
word=s1+s1
print(word)
if s2 in word:
    print("rotation")
else:
    print("not a rotation")