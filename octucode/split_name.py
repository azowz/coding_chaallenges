#input last name 

names = input("Enter the first and last name of your friends separated by a comma: ")
names = names.split(', ')

print(names)
print("\n".join(names))

first_last_name = []
for name in names:
    first_last = name.split(" ")
    first_last_name.append(first_last)

print(first_last_name)

# طباعة أول حرف من الاسم الأول والاسم الأخير بأحرف كبيرة
for i in first_last_name:
    first_initial = i[0][0].upper()  # أول حرف من الاسم الأول
    last_initial = i[1][0].upper()   # أول حرف من الاسم الأخير
    print(first_initial + ". " + last_initial + ". ")

# مثال على المدخلات: Ibrahim Abel, Tom Bandint, Emily Law, Cathy Yan, Mose Fasd, Azooz Hkeem

#Ibrahim abel, Tom Bandint, Emily Law, Cathy Yan, Mose Fasd, Azooz Hkeem
