print("WELCOME TO UNIT COVERTER!")
print("Here you can convert kilometers into mails.")

while True:
    #The program asks user to enter number of kilometers
    kms = input("enter kilometers: ")

    # Covert string into float
    kms = float(kms.replace(",", ".")) # se naredi tako da v sločajo da vporabnik da vejco namsto piko le ta ga zamenja ker pri flotih je obvezna pik ker drugače se program se sesuje.

    # the program coverts these klimoters into mails and prints them.

    miles = kms * 0.621371
    print(f"{kms} klimmeters is {miles} miles. ")

    #The program asks user if s/he d want to do another coversion.
    #If yes, repete  the above process (except the gretig).
    # if not, the programsays goodbey and stoops ("breake").

    choice = input("Wouold you like to do  another coverion (Y/N)? ")

    if choice == "N" or choice == "n" or choice == "no" or choice == "NO":
        print("Thank and goodbay!")
        breake

    