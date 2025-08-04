
person = input("Enter the names of attendees separated by commas:")
attendees = person.split(", ")
# ['alice', 'bob', 'charlie']
for i in attendees:
    print(i)
    cheek = input("Is this person attending? (yes/no):").lower()

    if cheek == 'yes' :
        print("attendance confirmed!\n------")
    elif cheek == 'no' :
        print("attendance not confirmed!\n------")
    else :
        print("Invalid input. Please enter yes or no.\n------")

            