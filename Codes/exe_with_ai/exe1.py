# Exercise 1: Guess the word
# 
# Create a variable secret_word = "python".
# Start a while True loop.
# Ask the user for a word with input.
# If it's correct, print "Correct!" and use break.
# Otherwise print "Wrong, try again!".

tabby = "Tabby"

while True:

    user = input("Enter your word: ")


    if tabby == user:
        print("Correct! ")
        break

    else:
        print("Wrong, try again!")

