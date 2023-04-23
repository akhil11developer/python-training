"""Write a Python program to get the Factorial number of given number.
    """
n = int(input("Enter a number"))
fac =1
i=1
while i<=n:
    fac =fac*i  #1*1 1*2 1*3 
    i=i+1      #1+2+3  = 6
print("factiorial number",fac) #=6


