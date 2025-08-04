import random

# توليد رقم PIN عشوائي للكمبيوتر كمجموعة من 4 أرقام
computer_PIN = str(random.randint(0, 9999)).zfill(4)

# طلب رمز PIN من المستخدم والتحقق من صحته
PIN = input("Enter a 4-digit PIN code:")

# التحقق من أن رمز PIN المدخل يتكون من 4 أرقام
if len(PIN) == 4 and PIN.isdigit():
    if PIN == computer_PIN:
        print("Success! PIN code matched.")
    else:
        print("Failure! PIN code did not match.")
        print(f"The Computer generated this PIN: {computer_PIN}")
else:
    print("Invalid input! Please enter a 4-digit PIN code.")
