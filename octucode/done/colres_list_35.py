colors = []

# طلب اللون الأول من المستخدم وإضافته إلى القائمة
color = input("Add the first color you like: ")
colors.append(color)

while True:
    add_more = input("Do you want to add another color? (yes or no): ")

    if add_more.lower() == "yes":
        color_other = input("Add the color you like: ")
        colors.append(color_other)
    else:
        break

# طباعة الألوان التي يحبها المستخدم
print("The colors you like are:")
print(colors)
