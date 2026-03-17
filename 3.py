yesbro=[]
for i in range(5):
    num=int(input("enter the number:"))
    print("the number is:",num)
    yesbro.append(num)
print(sorted(yesbro))
even=[]
for i in yesbro:
      if i%2==0:
        even.append(i)
print(even)
odd=[]
for i in yesbro:
    if i%2!=0:
        odd.append(i)
print(odd)
print("even num count is:",len(even))
print("odd num count is:",len(odd))

arr=[1,5,7,9,24]
print(max(arr))
print(min(arr))
print("logic is:", max(arr)-min(arr))

student={
    'name':'john',
    'age':20,
    'marks':{
        'maths':45,
        'english':90,
        'science':65
    }
}
for key,values in student.items():
    print(key,values)
for key,values in student['marks'].items():
    print(key,values)
    if values>=90:
        print(f"{key} is grade O")
    elif values>=75:
        print(f"{key} is grade A")
    elif values>=50:
        print(f"{key} is grade B")
    else:
        print(f"{key} failed")
print("student with highest marks is:", max(student['marks'],key=student['marks'].get))

yesss=[25,67,90,25,89,34,25,34,15,7,50] 
print(yesss)
above=[]
below=[]
equalto=[]
for i in yesss:
      if i>50:
          above.append(i)
      elif i<50:
            below.append(i)
      elif i==50:
            equalto.append(i)
      else:
            print("not found")
print("above 50:",above)
print("below 50:",below)
print("equal to 50:",equalto)
print(f"count of above 50: {len(above)}, count of below 50: {len(below)}, count of equal to 50: {len(equalto)}")

grocery={}
for i in range(3):
    item=input("enter the item name:")
    grocery[item]=int(input("enter the price:"))
print(grocery)
for key,values in grocery.items():
    print(key,values)
total=sum(grocery.values())
print("the total price is:",total)
print("most expensive item is:",max(grocery,key=grocery.get))
replaced=input("enter the item name to replace:")
if replaced in grocery:
    new_price=int(input("enter the new price:"))
    grocery[replaced]=new_price
    print(grocery)
else:
    print("item not found")