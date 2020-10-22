#asking user what track they are on and how many they would like to skip
user_current = int(input("What track are you currently on? "))
user_skip = int(input("How many tracks would you like to skip? "))

#Adding the track with the skip to get the new track 
track = user_current + user_skip
#If statement to track can revert to track 0 after track 11
if track > 11:
    print("You are now on track: 0 ")
else:
    print("You are now on track:", track)
    



            
