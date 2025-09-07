print("Temperature Warning System")
#Continues loop so that consumer can check the weather as many times as desired
while True:
    temp = input("Enter temperature: ")
    #Checks if the input is a digit
    if temp.isdigit():
        #Makes the input a integer
        temp=int(temp)
        #Compares input with 0
        if temp <= 0:
          print("Too cold ")
        #Compares the input with 100
        elif temp >= 100:
            print("Too hot")
        #Compares input to be between 64 and 75
        elif temp >= 64 and temp <= 75:
            print("Best temperature")
        #Prints if everything else is false
        else:
            print("The temperature is terrible right now")
    #If the input isn't a number
    else:
        print("Input has to be a number!")
 


