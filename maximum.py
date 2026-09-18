# Python program to find the maximum between two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("Maximum number is:", num1)
elif num2 > num1:
    print("Maximum number is:", num2)
else:
    print("Both numbers are equal.")