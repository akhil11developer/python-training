f = open("akhil.txt","r")

str = ""

for i in range(0,100):
    str = str + f.read(i) #store in variable to text
print(str)