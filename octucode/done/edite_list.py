list_things = [['Apples', 'Bananas'], ['Milk', 'Water']]
input("Press enter to change the content ...")

num = [1, 2, 3]

# تعديل المحتويات في القائمة
list_things[0].insert(0, 'Oranges')
list_things[0].append('Kiwis')

list_things[1].remove('Water')
list_things[1].append('Tea')
list_things[1].insert(0, 'Coffee')

# دمج قائمة الأرقام مع list_things
list_things.extend([num])

print("Here is the updated basket:")
print(list_things)
