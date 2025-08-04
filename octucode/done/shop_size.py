length = input("plese type length:\n")
width = input("plese type width:\n")
match = input("how much for 1 meter?:\n")

area = int(length) * int(width) 
pric = float(match) * area
print("the total area is :"  + str(area) )
print("give the guy:$" + str(pric) )

