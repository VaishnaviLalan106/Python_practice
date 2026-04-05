sets = input("Enter string: ")
print(sets)
setu=set()
found=False
for s in sets:
    if s in setu:
        print(f"{s} is first duplicate")
        found=True
        break
    else:
        setu.add(s)
if not found:
    print("no duplicate found")
        
