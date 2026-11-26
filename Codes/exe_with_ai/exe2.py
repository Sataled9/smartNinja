# Exercise 2: Guess with limited attempts
#
# Generate a secret number from 1 to 10 with random.randint.
# Create attempts = 0 and max_attempts = 3.
# In the loop, ask for a number and increase attempts by 1.
# If the guess is right, print "You win!" and break.
# If attempts == max_attempts, print "Game over" and the secret number, then break.
# Otherwise tell the user to try higher or lower.

import random

secret = random.randint(1, 10)

attemps = 0

max_attemps = (3)

while True:

    guess = int(input("Enter a number: "))

    attemps += 1

    if secret == guess:
        print("You win!")
        break

    if attemps == max_attemps:
        print("Game Over")
        print(f"The secret number was {secret}")
        break
    
    elif secret > guess:
        print("Try something Bigger")

    elif secret < guess:
        print("Try something Smaller") 