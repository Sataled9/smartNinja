#Homework 8.2 

# Variable called "secret", range between 1 and 20 

secret = 12 #intiger ker je brez navednic

#Users guess in a variabel called guess
guess = int(input("Enter your guess: ")) # "12" rešitev oziroma (string) -> (intiger)
#guess = int(guess)

#Check if your secret is equal to users secret 
if secret == guess:
    print("You ̌ve guessed it - congratulation!")

else:
    print("Sorry, your guess is not correct ... try again!")
