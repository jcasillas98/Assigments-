#player_actions.py


def check_play_again(user_input):
    #Your code here
    
    if user_input == "Y":
        print("Let the game begin!")
    elif user_input == "y":
        print("Let the game begin!")
    elif user_input == "N": 
        print("Thank you for playing! Hope you had fun.")
    elif user_input == "n": 
        print("Thank you for playing! Hope you had fun.")
    
    else:
        print("Invalid input")
    
    
    

check_play_again(input("Would you like to play again? Type Y for Yes or N for No: \n"))
