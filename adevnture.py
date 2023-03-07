name = input("Hello, May I know your name please? ")
interest = input(("Hey",name,"Do you wanna take this adventure? ")).lower()
if (interest == "yes"):
    answer = input("Let's start your adventure. You have walked till the end of a road, you want to take left/right? Type left for right as per your interest please ").lower()

    if (answer == "left"):
        answer = input("You have a park ahead to your left and a beach ahead to your right. Where do you want to go? Type park/beach accordingly ").lower()

        if (answer == "park"):
            print("Congratulations! You found a treasure")
        elif(answer == "beach"):
            answer = input("Do you wanna take a beach side walk or cruise? Type walk or cruise ").lower()
            
            if(answer == "walk"):
                print("You won a gift card. Yayyyy !!!!")
            elif(answer == "cruise"):
                print("You won a gift voucher")

        else:
            print("Invalid option. Sorry your adventure ends abruptly.")

    

    elif (answer == "right"):
        answer = input("You have a bridge to your left. You wanna take left or continue straight? Please type left or straight ").lower()

        if (answer == "left"):
            answer = input("You have a car and a bike infront of you. Please choose your means of transport by typing car/bike ").lower()
            if (answer == "car"):
                print("Surprise!! You won this car")
            elif(answer == "bike"):
                print("Sorry you won nothing")
            else:
                print("Invalid option. Sorry your adventure ends abruptly.")

        elif(answer == "straight"):
            print("Your journey ends at this concert. You have VIP entry to this. Please enjoy!!")
        else:
            print("Invalid option. Sorry your adventure ends abruptly.")


    else:
        print("Invalid option. Sorry your adventure ends abruptly.")
else:
    quit()
