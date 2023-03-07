import random
print("Hey there! Welcome")
interest = input("Are you interested in guessing the number game? ")
if (interest.lower() != "yes"):
    quit()
else:
    print("Cool then! Let's guess")
    print("Remember, you have only 3 chances")

number = random.randint(1,10)

i = 0
while (i < 3):
    attemptOne = int(input("Guess the number below 10 "))

    if (attemptOne == number):
        print("Congratulations! You guessed it right")
        break
    else:
        print("You guessed it wrong")
        i += 1    
        continue
        
else:
    print("Sorry you lost!!")
    print("The number was", number)

