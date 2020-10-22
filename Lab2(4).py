#Items and prices
pizza = int(8)
wings = int(7)
brownies = int(8)

#Welcome print
print("Hello, welcome to Julian's pizza planet")

#asking user how many of they items they would like
user_pizza = int(input("How many pizzas would you like? ($8 each): "))
user_wings = int(input("How many wings would you like? ($7 each): "))
user_brown = int(input("How many brownies would you like? ($8 each): "))

#claculating the cost of each item 
pizza_cost = user_pizza * pizza
wing_cost = user_wings * wings
brown_cost = user_brown * brownies

#calcualting the total price
total = pizza_cost + wing_cost + brown_cost

#printing result
print("Your total is:", "$",total)
print("Thank you! Have a nice day!")
print("We hope to see you again.")
      

