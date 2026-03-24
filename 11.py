import json
import os
store = {
    "apple": {"weight": 100, "price": 100},
    "banana": {"weight": 100, "price": 100},
    "rice": {"weight": 100, "price": 100},
    "milk": {"weight": 100, "price": 100}
}
def store_input():
    with open("store.json", "w") as f:
        json.dump(store, f)
def load_store():
    if not os.path.exists("store.json"):
        with open("store.json", "w") as f:
            json.dump(store, f)
        return store
    else:
        with open("store.json", "r") as f:
            return json.load(f)
store = load_store()
bill = {}
def shopping():
    while True:
        print("\n1.Add items\n2.View Bill\n3.Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            item = input("Enter item name:").lower()
            if item in store:
                weight = float(input("Enter weight:"))
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
                    print(f"{item} added: {weight}kg: ₹{total_price}")
                else:
                    print("Not enough stock")
            else:
                print("Item not found!")
        elif choice == 2:
            print("\n--bill--")
            total_amount = 0
            for item, details in bill.items():
                print(f"{item} - {details['weight']}kg - ₹{details['price']}")
                total_amount += details['price']
            print("Total =", total_amount)
        elif choice == 3:
            print("Thank you for shopping")
            break

shopping()
