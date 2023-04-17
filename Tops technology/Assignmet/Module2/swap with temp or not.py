a = int(input("Enter a number 1:"))
b = int(input("enter a number 2:"))

temp = a
a=b
b=temp

print(a)
print(b)

c=10
d=20
c,d =d,c

print("without temp",c)
print("without temp",d)