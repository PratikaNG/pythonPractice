import random

# print("Hello there!!")
# interest = input("Do you want to play \"Rock-Paper-Scissors\"? ")
# if(interest.lower() != "yes"):
#     quit()
# else:
#     print("Cool! Let's play")
computer_wins = 0
user_wins = 0
options = ["rock","paper","scissors"]


# print(computer_pick)
while True:
    user_pick = input("Select Rock/Paper/Scissors or q to quit ").lower()
    if (user_pick == "q"):
        break
    
    if (user_pick not in options):
        continue
    n = random.randint(0,2) 
    computer_pick = options[n]
    

    if (user_pick == "rock" and computer_pick == "scissors"):
        print("You won")
        print("Your opponent picked", computer_pick)
        user_wins += 1
    elif (user_pick == "paper" and computer_pick == "rock"):
        print("You win")
        print("Your opponent picked", computer_pick)
        user_wins += 1
    elif(user_pick == "scissors" and computer_pick == "paper"):
        print("You win")
        print("Your opponent picked", computer_pick)
        user_wins += 1
    elif(user_pick == computer_pick):
        print("You both picked same. Try again")
    else:
        print("You lost")
        print("Your opponent picked", computer_pick)
        computer_wins += 1
       
print("You won",user_wins,"times")
print("Computer won",computer_wins,"times")
print("Goodbye!!")        