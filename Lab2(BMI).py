#Asking user height and weight
user_pounds = int(input("What is your weight in pounds? "))
user_height = int(input("What is your height in inches? "))

#squaring the height
square = user_height * user_height

#multiplying the weight by 703
Mult = user_pounds * 703

#dividing the answer of the multiplication with the answer of the square
Div = Mult / square

print("Your BMI is",Div)

                  
