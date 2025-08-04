import random 

print("Welcome to the Coin Guessing Game! ")
print("Choose a method to toss the coin:")
print("1. using random.ranom()")
print("using random.randint()")

choice_guess = int(input("Enter your Guess (1 or 2):"))
choice_coin = input("Enter your Guess (Heads or Tails):")

if choice_guess == 1 :

    coin1 = random.random()

    if coin1 > 0.5 :
        computer_chois = "heads"
    elif coin1 < 0.5 :
        computer_chois = "tails"
    if choice_coin.lower == computer_chois: 
        print("You Win! ")
    
    else:
        print("You Lose! ")
        print(f"The computer's coin toss result was :{computer_chois} ")

if choice_guess == 2 :
    coin2 = random.randint(1,2)

    if coin2 == 1 :
        computer_chois2 = "heads"
    if coin2 == 2 :
        computer_chois2 = "tails"
    if coin2 == choice_coin.lower :
        print("You Win! ")
    else :
        print("You Lose! ")
        print(f"The computer's coin toss result was :{computer_chois2} ")

else : 
    print("Invalid Input! ")





