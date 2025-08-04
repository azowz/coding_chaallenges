area = input("Chose an area : (Cairo), (Alexan) or (Tanta)")

if area.lower() == "Cairo" : 
    print("Cairo is the capital of Egypt")
elif area.lower() ==  "alexan":
    print("Alexandria is the second largest city in Egypt")
elif area.lower() == "tanta":
    print("Tanta is the third largest city in Egypt")
else: 
  print(f"Invalid {area}")