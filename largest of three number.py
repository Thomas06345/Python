'''Author:Thomas Cherian
   date: 22-10-24
   python program:to find the largest of three numbers.'''
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1>num2 and num1>num3:
    print("The largest number is :",num1)
elif num2>num1 and num2>num3:
    print("The largest number is :", num2)
else:
    print("The largest number is :", num3)