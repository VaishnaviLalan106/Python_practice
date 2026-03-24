import json
store={
    "apple":{"weight": 0,"price":0},
    "banana":{"weight": 0,"price":0},
    "rice":{"weight": 0,"price":0},
    "milk":{"weight": 0,"price":0}
}
for key,values in store["apple"].items():
    store["apple"]["weight"]=int(input("Enter weight of apple:"))
    store["apple"]["price"]=weight*store["apple"]["price"]  
for key,values in store["banana"].items():
    store["banana"]["weight"]=int(input("Enter weight of banana:"))
    store["banana"]["price"]=weight*store["banana"]["price"]  
for key,values in store["rice"].items():
    store["rice"]["weight"]=int(input("Enter weight of rice:"))
    store["rice"]["price"]=weight*store["rice"]["price"]  
for key,values in store["milk"].items():
    store["milk"]["weight"]=int(input("Enter weight of milk:"))
    store["milk"]["price"]=weight*store["milk"]["price"]  

print(store)
def store_input():
    with open("store.json","w") as f:
        json.dump(store,f)
def load_input():
    with open("store.json","r") as f:
        data=json.load(f)
        print(data)
store_input()
load_input()


bill={}
def shopping():
    while True:
        print('''welcome to vaishu's mart
        1.add items
        2.view items
        3.update items
        4.delete items
        5.exit
        ''')
        choice=int(input("Enter your choice:"))
        if choice==1:
            print('''our present stock is : 
            1. apple
            2. banana
            3. rice
            4. milk''')
            item=int(input("Enter your choice:"))
            weight=int(input("Enter weight:"))
            if item==1:
                bill["apple"]=store["apple"]["price"]
                appleprice=weight*store["apple"]["price"]
                print(appleprice)
                bill["apple"]=appleprice
            elif item==2:
                bill["banana"]=store["banana"]["price"]
                bananaprice=weight*store["banana"]["price"]
                print(bananaprice)
                bill["banana"]=bananaprice
            elif item==3:
                bill["rice"]=store["rice"]["price"]
                riceprice=weight*store["rice"]["price"]
                print(riceprice)
                bill["rice"]=riceprice
            elif item==4:
                bill["milk"]=store["milk"]["price"]
                milkprice=weight*store["milk"]["price"]
                print(milkprice)
                bill["milk"]=milkprice
        elif choice==2:
            for key,values in bill.items():
                print(f"{key}:{values}")
        elif choice==3:
            print('''our present stock is : 
            1. apple
            2. banana
            3. rice
            4. milk''')
            item=int(input("Enter your choice:"))
            weight=int(input("Enter weight:"))
            if item==1:
                bill["apple"]=store["apple"]["price"]
                appleprice=weight*store["apple"]["price"]
                print(appleprice)
                bill["apple"]=appleprice
            elif item==2:
                bill["banana"]=store["banana"]["price"]
                bananaprice=weight*store["banana"]["price"]
                print(bananaprice)
                bill["banana"]=bananaprice
            elif item==3:
                bill["rice"]=store["rice"]["price"]
                riceprice=weight*store["rice"]["price"]
                print(riceprice)
                bill["rice"]=riceprice
            elif item==4:
                bill["milk"]=store["milk"]["price"]
                milkprice=weight*store["milk"]["price"]
                print(milkprice)
                bill["milk"]=milkprice
            else:
                print("Invalid choice")
        elif choice==4:
            item=str(input("Enter item to remove:")).lower()
            for i in bill:
                if i==item:
                    del bill[i]
                    print(f"{item} is removed")
                    break
            else:
                print("Item not found")
        elif choice==5:
            print("Thank you for shopping with us")
            break
shopping()
print(bill)
def overall():
    with open("bill.json","w") as f:
        json.dump(bill,f)
overall()
def load_bill():
    with open("bill.json","r") as f:
        data=json.load(f)
        print(data)
load_bill()