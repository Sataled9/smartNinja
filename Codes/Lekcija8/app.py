""" 
with open("Test.txt", "r") as test_file:
    content = test_file.read()
    print(content)

#Second methode this i s better (best practise!)

test_file = open("Test.txt", "r")

content = test_file.read()
print(content)

test_file.close()

with open("record.txt", "w") as record_file: #mogu be se odpreti sam datoteko na ni 
    record_file("Hellow record file!")
""" 


import random

secret = random.randint(1, 20)

attemps = 0

with open("record.txt", "r") as record_file:
    record = int(record_file.read()) # "1000" - Najboljši rezultat
    print("Welcome to the game!")
    print(f"Current best score: {record}")

#secret = 12 #intiger ker je brez navednic



# Whaile Loop + keyword BRAKE
#while secret_not_found == True:

while True:

 #Users guess in a variabel called guess
    guess = int(input("Enter your guess: ")) # "12" rešitev oziroma (string) -> (intiger)
    #guess = int(guess)
    attemps += 1

    #Check if your secret is equal to users secret 
    if secret == guess:
        print("You ̌ve guessed it - congratulation!" )
        #print(f"Secret number was {secret}. ")
        print(f"attemps needet... {attemps}. ")
        
        if attemps < record:
            with open("record.txt", "w") as record_file:
                record_file.write(str(attemps)) # "7 > 7"     
        
            
        break #stem prekinemo igro oz enkrat ko najde število se zanka zakluči. "recursia"

    elif secret > guess:
        print("Your guess is nt correct ... try smomething bigger!")

    elif secret < guess:
        print("Your guess is not correct ...try something smaller!")
    
    else:
        print("Sorry, your guess is not correct ... try again!")
