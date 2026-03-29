#shoud be done to practice functions and modules in python

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

def addition():
    result = num1 + num2
    return print(f"{num1} Plus {num2} = {result}")

def substraction():
    result = num1 - num2
    return print(f"{num1} Minus {num2} = {result}")

def multiplication():
    result = num1 * num2
    return print(f"{num1} Times {num2} = {result}")

def devision():
    result = num1 / num2
    return print(f"{num1} Devide {num2} = {result}")

addition()
substraction()
multiplication()
devision()