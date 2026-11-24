
"""
print (15 % 5) # 15 / 5, ostanke 0 ######## se imenuje modulo % vren ostanke deljenja

print (15 % 4) # 15 / 4 = 3 ostanek(modul) 3

print (3 % 3) # 3 / 3 = 2 Ostanke(modul) 0 

print (5 % 3) # 5 / 3 = 1 Ostanke(modul) 2

"""
# FizzBuzz exercise
number = int(input("Enter any number between 1 and 100: "))

for x in range(1, number + 1): # + 1 je do 10 od 0 - 10
    if x % 3 == 0 and x % 5 == 0:
        print("Fizzbuzz")

    elif x % 3 == 0:
        print("Fizz")

    elif x % 5 == 0:
        print("Buzz")

    else:
        print(x)