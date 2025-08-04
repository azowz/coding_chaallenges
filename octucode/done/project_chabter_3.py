print ("""

██╗░██████╗██╗░░░░░░█████╗░███╗░░██╗██████╗░
██║██╔════╝██║░░░░░██╔══██╗████╗░██║██╔══██╗
██║╚█████╗░██║░░░░░███████║██╔██╗██║██║░░██║
██║░╚═══██╗██║░░░░░██╔══██║██║╚████║██║░░██║
██║██████╔╝███████╗██║░░██║██║░╚███║██████╔╝
╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░

""")

print("Welcome to my island!")
print("There are two doors in front of you . 🚪 a red door and 🚪 a blue door ")
door_choes = input("Which door do you want to open? ")

if door_choes.lower() == "red" : 
    
    print("Great! now you entered a room.")
    print("you found three boxes:  🎁 white, 🎁 black, 🎁 green ")
    box_choes = input("Which box do you want to open? ")


    if box_choes.lower() == "white" :
        print("Oops! You opened a box filled with snakes 🐍🐍🐍")
    elif box_choes.lower() == "black" :
        print("Oops! You opened a box filled with spiders 🕸️🕸️🕸️")
    elif box_choes.lower() == "green":
         print("Congratulations! You found the treasure!🪙🪙🪙") 
    else:
        print("Invalid choice! 🤦‍♂️ ♂️ 🤦‍♂️ ♂️ 🤦‍♂️ ")    

elif  door_choes.lower() == "blue " :   
    print("Oops! You chose the crocodile door. 🐊🐊🐊")
    print("Game over!")

else :
    print("Invalid choice! 🤦‍♂️ ♂️ 🤦‍♂️ ♂️ 🤦‍♂️ ")