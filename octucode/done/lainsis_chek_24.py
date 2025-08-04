age = int (input ("how old are you ?") )
lainses = input("do you have lainses ? \n yes  or no ")

if age >= 18 and lainses.lower() == "yes" : 
    print("you can drive")
elif age <18 or lainses.lower() == "no" :
    print ("you can't drive")    
else :
    print(f"rowng write {lainses}")   