print("Hello there !!")
interest = input("Do you want to play this quiz? ")
if (interest.lower() == "yes"):
    print("Cool! Let's play :)")
else:
    quit()
score = 0
q1 = input("CPU stands for? ")
if (q1.lower() == "central processing unit"):
    print("That's Correct!")
    score += 1
else:
    print("Sorry, that's incorrect")
    score -= .5

q2 = input("Which is the largest continent of the Earth? ")
if (q2.lower() == "asia"):
    print("That's Correct!")
    score += 1
else:
    print("Sorry, that's incorrect")
    score -= .5

print("Your score is " + str(score))
