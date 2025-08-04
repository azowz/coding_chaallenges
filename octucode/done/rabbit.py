print("Welcome to place the rabbit")

rabbit = [["f" , "f", "f"] ,["f", "f", "f"], ["f", "f", "f"]]
# طباعة الشبكة
for row in rabbit:
    print(row)

print("Where should the rabbit go?")
place = input("Please choose a row and a column")
row , colom = int(place[0])-1 , int(place[1]) -1
rabbit[row ] [colom]= 'r'

# طباعة الشبكة
for row in rabbit:
    print(row)



