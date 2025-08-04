library = []

# طلب اللون الأول من المستخدم وإضافته إلى القائمة
book = input("enter the name of a book you own : ")
library.append(book)


while True:
    add_more = input("enter the name of another book you own? (or press 'enter' to  skip): ")

    if add_more:
        library.append(add_more)
    else:
        break

# طباعة book التي يحبها المستخدم
print(f"yur Library:{library}")



future_book = []

# طلب اللون الأول من المستخدم وإضافته إلى القائمة
book = input("enter the name of a book you wish to have in the future (or press 'enter' to  skip): ")
if book :
    future_book.append(book)

    while True:
        add_more = input("enter the name of another book you wish to have ? (or press 'enter' to  skip): ")

        if add_more:
             
             future_book.append(add_more)
        else:
             break

# طباعة book التي يحبها المستخدم
    print(f"yur future Library:{future_book}")


# =========================================================
## transfar form wishlist to library list
book = input("enter the name of a book you wish to have in the future (or press 'enter' to  skip): ")
if book in future_book :
    library.append(book)
    future_book.remove(book)

    while True:
        add_more = input("enter the name of another book you wish to have ? (or press 'enter' to  skip): ")
        if book in future_book :
         library.append(book)
         future_book.remove(book)
        else:
             break


#print library list and wh
    print(f"yur future Library:{library}")
    print(f"Updated Library:{future_book}")

    book = input("enter the name of a book you wish to have in the future (or press 'enter' to  skip): ")
    if book in library :
            library.remove(book)
    print(f"Final Library after Donations:{library}")        
             



