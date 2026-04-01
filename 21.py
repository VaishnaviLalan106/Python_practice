""" sent="abcabcbb"
print(sent)
sets=set(sent)
print(sets)                  #i tried to fin unique characters ,not the longest substring my mistake
curve=0
for i in range(len(sent)):
    if sent==sets:
        print(f"longest substring without repeating characters is {len(sets)}")
        break
    else:
        curve=curve+1
        print(f"longest substring without repeating characters is {len(sets)}")
        break """


sent="pwwkew"

longest=0
for i in range(len(sent)):
    seen=set()
    for j in range(i,len(sent)):
        if sent[j] in seen:
            break
        seen.add(sent[j])
    longest=max(longest,len(seen))
print(f"longest substring without repeating characters is {longest}")