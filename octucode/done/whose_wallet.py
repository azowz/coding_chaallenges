import random

print("Welcome to 'Whose Wallet?'")
print("You will give me a list of names, and I will pick a person to pay.")

names_string = input("If you're ready, enter the names separated by a comma: ")
names = names_string.split(", ")

# توليد قيمة عشوائية بين 0 و 1
propelaty = random.random() 

# حساب احتمالية اختيار كل شخص
choes = 1 / len(names)

# اختيار شخص لدفع الفاتورة بناءً على القيمة العشوائية
for i in range(len(names)):
    if propelaty < choes * (i + 1):
        print(f"Please ask '{names[i]}' to take their wallet out. Dinner is on them!")
        break

print("Random value used for selection:", propelaty)
print("Probability interval per person:", choes)




# very long 

print("Welcome to 'Whose Wallet?'")
print("You will give me a list of names, and I will pick a person to pay.")

names_string = input("If you're ready, enter the names separated by a comma: ")
names = names_string.split(", ")

lenghth = len(names) - 1
# توليد قيمة عشوائية بين 0 و 1
propelaty = random.randint(0,lenghth)

print