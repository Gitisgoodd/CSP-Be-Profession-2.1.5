
#Title of the program
print("----Grade Checker----")
age=0
#While loop so that it keeps on looping until a integer is chosen
while age == 0:
 grade_input  = input("Enter your test score: ")
 #When integer is chosen, it converts the string to a integer
 if grade_input.isdigit():
        grade = int(grade_input)
      
        #All of these compare the integer to a letter grade
        if grade >= 90:
            print("You got a A")
        elif grade < 90 and grade >= 80:
            print("You got a B")
        elif grade < 80 and grade >= 70:
            print("You got a C")
        elif grade < 70 and grade >= 60:
            print("You got a D")
        #If all the other options return false
        else:
            print("Sorry, you got a failing grade")    
# If a input isn't a number
 else:
    print("Sorry, input a number from 0-100")        
        

