#asking the user for n 
user_number = int(input("What is the number of sides of the polygon? "))
#subtracting n by 2
sub = user_number - 2

#multiplying the answer to 180
Multi = sub * 180

#dividing the answer with n
Div = Multi / user_number

#printing the answer
print("The inerior angle of the polygon is:", Div)
