"""
Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5
    """


num1 = int(input("enter number 1:"))
num2 = int(input("enter number 2"))

if  abs(num1-num2) == 5 or num1+num2 ==5:
    print("right")
else:
    print("wrong")