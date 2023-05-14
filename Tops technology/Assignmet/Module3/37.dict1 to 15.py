"""Write a Python script to print a dictionary where the keys are numbers
between 1 and 15."""

#first
d=dict()
for x in range(1,16):
    d[x]=x**2  #x is key x**2 = key multiple of value 
print(d)  

