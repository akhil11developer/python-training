""" accept two numbers and check entered number is positive or negative"""

num = int(input("ENTER A NUMBER1: "))
num2 = int(input("enter number 2: "))

if num and num2>0:
    print("value is postive")
elif num and num2<0:
    print("value is negative")   
else :
    print("value is zero") 
