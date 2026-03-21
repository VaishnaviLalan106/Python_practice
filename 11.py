import json
store={
     "apple":{"weight":100,"price":100},
     "banana":{"weight":100,"price":100},
     "rice":{"weight":100,"price":100},
     "milk":{"weight":100,"price":100}   
}
print(store)
def store_input():
    with open("store.json","w") as f:
        json.dump(store,f)
def load_store():
    try:
        with open("store.json", "r") as f:
            return json.load(f)
    except:
        return {
            "apple":{"weight":100,"price":700},
            "banana":{"weight":100,"price":700},
            "rice":{"weight":100,"price":700},
            "milk":{"weight":100,"price":700}  
        }
store=load_store()
bill={}
def shopping():
    while True:
        print("1.Add items\n 2. View Bill\n 3. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            item=input("enter item name:").lower()
            if item in store:
                weight = float(input("enter weight:"))

                if weight <= store[item]["weight"]:
                    total_price = weight * store[item]["price"]

                    store[item]["weight"] -= weight
                    store_input()
                    if item in bill:
                        bill[item]["weight"] += weight
                        bill[item]["price"] += total_price
                    else:
                        bill[item] = {
                            "weight": weight,
                            "price": total_price
                        }

                        print(f"{item} added. weight={weight} Price = {total_price}")

            else:
                print("Not enough stock!")

        elif choice == 2:
             print("\n--- BILL ---")
             total_amount = 0
             for item, details in bill.items():
                print(f"{item} - {details['weight']}kg - ₹{details['price']}")
                total_amount += details['price']
             print("Total =", total_amount)
        
        else:
            print("Thank you for shopping with us")
            break
shopping()


