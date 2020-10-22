#This program will take a password from the user and print an appropriate message
#The 'in' keyword checks to see if a value exists somewhere in the given string.

greeting = input("Hello, possible pirate! What's the password?")
value = "Arrr!"
if value in greeting :
	print("Go away, pirate.")
else:
        print("Greetings, hater of pirates!")
