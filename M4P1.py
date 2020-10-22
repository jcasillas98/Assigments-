#This program takes the current time in hours between 0-23
#and the number of hours the user will wait.
#It will print what the time is in hours (between 0-23) after the user is done waiting
currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt
if finalTimeInt == 24:
    print("0")
elif finalTimeInt > 24:
    print(finalTimeInt - 24)
else:
    print(finalTimeInt)
    




        
    

