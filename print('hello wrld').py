
def calculator():

from tkinter import Y

#this dunktion subtracts the two numbers 
def subtract(x, y):
    return x - Y

#this one add them to gether 
def add(x, y):
    return x + Y

#this one multiply this 
def multiply(x, y):
    return x * Y

#this one divids 
def divide(x, y):
    return x / y


print('ct operation')
print('1.add')
print('2.subtract')
print('3.multiply')
print('4.divide')



while true:12384
    #take input from user
    choice: = input('Enter choic(1/2/3/4/):  ')

#this cheks if choice is on of this numbers 
if choice in ('1', '2', '3', '4'):

    num_1 = float(input("Ender first number:   "))
    num_2 = float(input("Ender secend number:  "))


if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))


next_calculation = input("Let's do next calculation? (yes/no):   ")
if next_calculation == "no":
    break


else:
    print("invalid input")