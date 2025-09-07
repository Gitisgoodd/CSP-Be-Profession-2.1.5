#Project Reflection
# “What was the hardest bug to fix, and why?”
# The hardest bug to fix was the grade checker, where there were lots of places where it could have been a lot more simplifier. So I had to look at the whole code and use logic to see what places weren't needed and which were needed.

# “How did testing help you find logical problems?”
# Testing helped me find logical problems since after testing the code for a couple of times, I would see which places would be correct, and which places don't make that much logical sense.

# “What is one thing you’ll do in future projects to avoid writing sloppy code?”
# One thing that I will do in future projects to aviod writing sloppy code is to dedicate one day or a good amount of time just to review and go over the code to see which parts could be ommitted out since it would be unnecessary.

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
#If the input is not in the range of 1-6 or not a number
    else:
        print ("An invalid input, please put a number between 1-6 ")
