
x = int(input("Vnesi prvo število: "))

operation = input ("Izberi matično operacijo(+, -, *, /): ")

y = int(input("Vnesi drugo število: "))

if operation == "+":
    result = x + y
    print(f"Rezultat enačbe {x} {operation} {y} = {result}.")

elif operation == "-":
    result =  x - y 
    print(f"Rezultat enačbe {x} {operation} {y} = {result}.")

elif operation == "*":
    result =  x * y
    print(result)

elif operation == "/":
    result = x / y
    print(result)

else: 
    print("Nekaj je šlo narobe, poskusi ponovno") 


"""
#Homework 8.3: Calculator
num1 = float(input("Enter the first number: "))

operation = input("Enter the operation (+, -, *, /): ")

num2 = float(input("Enter the second number: "))

if operation == "+":
    print(num1 + num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "*":
    print(num1 * num2)

elif operation == "/":
    print(num1 / num2)

else:
    print("I do not recognise this operation.")
"""