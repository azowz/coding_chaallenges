print("**** Welcome to ishop calculator ****")

item = []
price = []

items = int (input("How many items are there in yout baskt today ?"))

for i in range(items):
        item_name = input(f"Enter item name number {i}: ")
        item.append(item_name)
        pric = int(input(f"What is the price of {item_name}"))
        price.append(pric)

show1 = input("Would you like to see your entire basket items ?")
if show1 == "yes":
        print(item)

show2 = input("Would you like to see how nuch it'll cost ?")
if show2 == "yes":
        print(sum(int (pric)))



