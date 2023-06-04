"""What is File function in python? What is keywords to create and write
file. 
"""

f= open("akhil.txt","w") #create a new file with write mode .

n = input("Enter your name : ")  
f.write(n)  #we can store data in file
f.close()

