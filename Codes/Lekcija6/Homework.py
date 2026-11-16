#Homework 8.2 

# Variable called "secret", range between 1 and 20 

secret = 12 #intiger ker je brez navednic

# FOR (for-in) LOOP
for x in range(3): # trikrat ponivi to kodo (spodaj pa z tipko TAB se premakne vse v desno in je v zanki(loop))

    #Users guess in a variabel called guess
    guess = int(input("Enter your guess: ")) # "12" rešitev oziroma (string) -> (intiger)
    #guess = int(guess)

    #Check if your secret is equal to users secret 
    if secret == guess:
        print("You ̌ve guessed it - congratulation!")
        break #stem prekinemo igro oz enkrat ko najde število se zanka zakluči. "recursia"

    else:
        print("Sorry, your guess is not correct ... try again!")
