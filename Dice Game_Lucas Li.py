#Title of the program
print("Dice Game Result Checker")

while True :
    roll = input("Enter dice roll (1-6): ")
#Checks if the number inputed is a digit and between 1 and 6
    if roll.isdigit() and "1"<= roll <= "6":
#Converts the string to an integer
        roll= int(roll)
#All of these check to see what the inputed number corresponds to 
        if roll ==6 or roll==5:
            print("You win big!")
            roll=+1
        elif roll ==4 or roll==3 :
            print("You win something that is a pretty good amount.")
            roll=+1
        elif roll==2 or roll==1:
            print("You win something small")
#If the inpute is not in the range of 1-6 or not a number
    else:
        print ("An invalid input, please put a number between 1-6 ")
