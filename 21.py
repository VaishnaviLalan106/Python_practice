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


