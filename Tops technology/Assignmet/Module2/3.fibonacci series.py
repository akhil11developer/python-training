""" Write a Python program to get the Fibonacci series of given range.
"""
     
fibonacci =10 
x= 0 
y=1
z= 0

while z<=fibonacci: #condition is right, loop is start.
     print(z)  #0 1 1 2 3 5
     x= y #1 0 1 1 2 3
     y= z #0 1 1 2 3 5
     z = x+y #1+ 1+2+ 3+ 5
     