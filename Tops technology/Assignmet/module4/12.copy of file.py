"""Write a Python program to copy the contents of a file to another file."""

# open both files
f= open('akhil.txt','r') 
f1=open('second.txt','w') 
	
for line in f:
	f1.write(line)
